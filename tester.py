# class Route:
#     def __init__(self, depot: str = "", route: list = [], distance: int = 0, time: int = 0):
#         self.depot = depot
#         self.route = route
#         self.distance = distance
#         self.time = time
#         self.stops = len(route)
    
#     def set_distance(self, distance: int):
#         self.distance = distance

#     def set_time(self, time: int):
#         self.time = time

#     def add_stop(self, stop):
#         self.route.append(stop)
#         self.stops += 1
    
#     def remove_stop(self, num):
#         self.route.pop(num)
#         self.stops -= 1

#     def find_stop(self, stop):


#         return self.route.index(stop)
# import sqlite3
# connection = sqlite3.connect("student.db")
# cursor = connection.cursor()
# routeAmt = len(cursor.execute("SELECT RouteID FROM routes").fetchall())-1
# response = cursor.execute("SELECT RouteID, Address, StudentID, Name FROM students ORDER BY RouteID, RouteOrder").fetchall()
# routes = [[] for _ in range(routeAmt)]
# for address in response:
#     routes[address[0]].append((address[2], address[3], address[1]))

# print(list([x[2] for x in y]for y in routes))

import googlemaps

class Graph:
    def __init__(self, time_graph: dict = {}, dist_graph: dict = {}, nodes: list = [], depot: str = ""):
        self.time_graph = time_graph
        self.dist_graph = dist_graph
        self.depot = depot
        self.nodes = nodes

    def add_dist_edge(self, node1, node2, weight):
        """Adds an edge on the distance graph, directed from node1 to node2"""
        if node1 not in self.dist_graph:
            self.dist_graph[node1] = {}
        self.dist_graph[node1][node2] = weight

    def add_time_edge(self, node1, node2, weight):
        """Adds an edge on the time graph, directed from node1 to node2"""
        if node1 not in self.time_graph:
            self.time_graph[node1] = {}
        self.time_graph[node1][node2] = weight

    def calc_distance(self, route: list):
        """Adds up all the distance weights of one route"""
        distance = 0
        for address_index in range(len(route)-1):
            distance += self.dist_graph[route[address_index]][route[address_index+1]]
        distance += self.dist_graph[self.depot][route[0]] + self.dist_graph[route[-1]][self.depot]
        return distance
    
    def calc_time(self, route: list):
        """Adds up all the time weights of one route"""
        time = 0
        for address_index in range(len(route)-1):
            time += self.time_graph[route[address_index]][route[address_index+1]]
        time += self.time_graph[self.depot][route[0]] + self.time_graph[route[-1]][self.depot]
        return time
    
    def find_distance(self, address1, address2):
        """Edge from address1 to address2 on dist_graph"""
        return self.dist_graph[address1][address2]
    
    def dist_edges(self, address1):
        """Returns a dict of edge weights from address1 to all other nodes"""
        return self.dist_graph[address1]
    
    def find_time(self, address1, address2):
        """Edge from address1 to address2 on time_graph"""
        return self.time_graph[address1][address2]
    
    def time_edges(self, address1):
        """Returns a dict of edge weights from address1 to all other nodes"""
        return self.time_graph[address1]
    
    def create_graph(self):
        gmaps = googlemaps.Client(key="AIzaSyDE2qaxHADLeBQO1zLqfDIasLOalcHWHi0")
        splitNodes = [self.nodes[i:i+1] for i in range(0, len(self.nodes), 10)] # The API can only handle 100 connections at a time, so 10x10
        for splitChunk1 in splitNodes:
            for splitChunk2 in splitNodes:
                result = gmaps.distance_matrix(splitChunk1, splitChunk2, mode="driving")
                for num1, row in enumerate(result["rows"]):
                    for num2, rowData, in enumerate(row["element"]):
                        if rowData["status"] != "OK":
                            raise Exception("Address not found")
                        elif splitChunk1[num1] == splitChunk2[num2]:
                            continue
                        self.add_dist_edge(splitChunk1[num1], splitChunk2[num2], rowData["distance"]["value"])
                        self.add_time_edge(splitChunk1[num1], splitChunk2[num2], rowData["duration"]["value"])

        
        self.nodes.append(self.depot)
        for address in self.nodes:
            for address2 in self.nodes:
                if address == address2: continue
                weight = gmaps.directions(address, address2, mode="driving")[0]["legs"][0]["distance"]["value"]
                self.add_dist_edge(address, address2, weight)
                weight = gmaps.directions(address, address2, mode="driving")[0]["legs"][0]["duration"]["value"]
                self.add_time_edge(address, address2, weight)
        self.nodes.pop()

    def get_nodes(self):
        return self.nodes
    
    def get_depot(self):
        return self.depot