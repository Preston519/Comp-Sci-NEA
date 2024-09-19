import sqlite3
import googlemaps
import sys

class Graph:
    def __init__(self, graph: dict = {}, nodes: list = [], depot: str = "Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ"):
        self.graph = graph
        self.nodes = nodes
        self.depot = depot

    def add_edge(self, node1, node2, weight): # A directed link from node1 to node2
        """Adds an edge on the graph, directed from node1 to node2"""
        if node1 not in self.graph:
            self.graph[node1] = {}
        self.graph[node1][node2] = weight

    def calc_distance(self, route: list):
        """Adds up all the weights of one route"""
        distance = 0
        for address_index in range(len(route)-1):
            # print(address_index)
            # print(route[address_index])
            distance += self.graph[route[address_index]][route[address_index+1]]
        return f"{distance//1000}km {distance%1000}m"

def create_graph():
    while True:
        sortparam = input("Make routes based on (D)istance or (T)ime? ").upper()
        if sortparam == "D":
            sortingmethod = "distance"
            break
        elif sortparam == "T":
            sortingmethod = "duration"
            break
    gmaps = googlemaps.Client(key="AIzaSyDE2qaxHADLeBQO1zLqfDIasLOalcHWHi0")
    # gmaps = googlemaps.Client(key="AIza") # Key that doesn't work
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()
    response = cursor.execute("SELECT Address FROM addresses")
    # cursor.execute("CREATE TABLE movie(title, year, score)")
    # print(response.fetchall()[0][0])
    nodes = list(map(lambda x: x[0], response.fetchall())) + ["Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ"]
    address_map = Graph(nodes=nodes)
    # print(list(nodes))
    for address in nodes:
        # print(address)
        for address2 in nodes:
            # print(address2)
            if address == address2: continue
            try:
                weight = gmaps.directions(address, address2, mode="driving")[0]["legs"][0][sortingmethod]["value"]
            except googlemaps.exceptions.ApiError:
                print("Invalid address input")
                sys.exit()
            address_map.add_edge(address, address2, weight)
    return address_map

if __name__ == "__main__":
    print(create_graph().graph)