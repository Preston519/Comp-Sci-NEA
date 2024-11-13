import googlemaps
from flask import Flask, request, render_template
import sqlite3
import csv
from os import remove

app = Flask(__name__)

class Graph:
    def __init__(self, time_graph: dict = {}, dist_graph: dict = {}, nodes: list = [], depot: str = "Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ"):
        self.time_graph = time_graph
        self.dist_graph = dist_graph
        self.depot = depot
        self.nodes = nodes
        self.length = len(nodes)

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
        # return f"{distance//1000}km {distance%1000}m"
        return distance
    
    def calc_time(self, route: list):
        """Adds up all the time weights of one route"""
        time = 0
        for address_index in range(len(route)-1):
            time += self.time_graph[route[address_index]][route[address_index+1]]
        time += self.time_graph[self.depot][route[0]] + self.time_graph[route[-1]][self.depot]
        # return f"{distance//1000}km {distance%1000}m"
        return time
    
    def find_distance(self, address1, address2):
        return self.dist_graph[address1][address2]
    
    def find_time(self, address1, address2):
        return self.time_graph[address1][address2]
    
    def create_graph(self):
        gmaps = googlemaps.Client(key="AIzaSyDE2qaxHADLeBQO1zLqfDIasLOalcHWHi0")
        self.nodes.append(self.depot)
        for address in self.nodes:
            for address2 in self.nodes:
                if address == address2: continue
                weight = gmaps.directions(address, address2, mode="driving")[0]["legs"][0]["distance"]["value"]
                self.add_dist_edge(address, address2, weight)
                weight = gmaps.directions(address, address2, mode="driving")[0]["legs"][0]["duration"]["value"]
                self.add_time_edge(address, address2, weight)
        self.nodes.pop()
        # self.nodes.pop(0) # Remove the first item, which should be the depot

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

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        depot = request.form["depot"]
        file = request.files["addresses"]
        constraint = request.form["constraint"]
        maximum = int(request.form["maximum"])
        file.save(file.filename)
        with open(file.filename) as addresses:
            data = list(csv.reader(addresses))
            connection = sqlite3.connect("student.db")
            cursor = connection.cursor()
            cursor.executemany("INSERT INTO students(StudentID, Name, Address, Year, RouteID) VALUES(?, ?, ?, ?, -1)", data)
            cursor.execute("INSERT INTO students(StudentID, Name, Address, Year, RouteID) VALUES(-1, 'Depot', ?, -1, -1)", (depot,))
            connection.commit()
            connection.close()
            processing(list(row[2] for row in data), depot, constraint, maximum)
        remove(file.filename)
        return render_template('finished.html')
    return render_template('index.html')

@app.route('/maps')
@app.route('/maps/')
def mapdisplay():
    data, routes, depot = fetch_data()
    embeds = routes_to_embed(routes, depot)
    return render_template('mapdisplay.html', maps=embeds, data=data, len=len(data))

def processing(nodes: list, depot: str, constraint: str, maximum: int):
    connection = sqlite3.connect("student.db")
    cursor = connection.cursor()
    graph = Graph(nodes=nodes, depot=depot)
    graph.create_graph()
    if constraint == "distance":
        from final_heuristics import two_opt, saving
    elif constraint == "time":
        from final_time_heuristics import two_opt, saving
        maximum *= 60
    sav_routes = saving(graph, maximum)
    topt_routes = []
    for route in sav_routes:
        topt_routes.append(two_opt(graph, route))
    connection = sqlite3.connect("student.db")
    cursor = connection.cursor()
    for routeID, route in enumerate(topt_routes):
        cursor.execute("INSERT INTO routes VALUES (?, ?, ?, ?)", (routeID, graph.calc_distance(route), graph.calc_time(route), len(route)))
        # print(cursor.execute("SELECT * FROM routes").fetchall())
        # for point in range(len(sav_routes[routeID][1:-1])):
        for n, point in enumerate(route):
            cursor.execute("UPDATE students SET RouteID = ?, RouteOrder = ? WHERE Address = ?", (routeID, n+1, point))
    connection.commit() # ALWAYS COMMIT dangit
    connection.close()

def fetch_data():
    connection = sqlite3.connect("student.db")
    cursor = connection.cursor()
    routes = [[] for _ in range(len(cursor.execute("SELECT RouteID FROM routes").fetchall())-1)] # If you use multiplication here it does pointer magic and makes them all the same list
    data = []
    response = cursor.execute("SELECT RouteID, Address FROM students ORDER BY RouteID, RouteOrder").fetchall()
    depot = response.pop(0)[1]
    for address in response:
        routes[address[0]].append(address[1])
    response = cursor.execute("SELECT Distance, Time, Stops FROM routes WHERE RouteID != -1 ORDER BY RouteID").fetchall()
    for info in response:
        data.append(info)
    connection.close()
    return data, routes, depot

def routes_to_embed(routes: list[list[str]], depot: str):
    embeds = []
    depot = depot.replace(", ", ",").replace(" ", "+")
    for route in routes:
        for address in route:
            # address: str
            route[route.index(address)] = address.replace(", ", ",").replace(" ", "+")
        embeds.append(f"https://www.google.com/maps/embed/v1/directions?key=AIzaSyDE2qaxHADLeBQO1zLqfDIasLOalcHWHi0&origin={depot}&destination={depot}&waypoints={'|'.join(route)}")
    return embeds

@app.route('/reset')
@app.route('/reset/')
def reset():
    connection = sqlite3.connect("student.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE students SET RouteID = -1, RouteOrder = ?", (None, ))
    cursor.execute("DELETE FROM routes WHERE RouteID != -1")
    cursor.execute("DELETE FROM students")
    connection.commit()
    connection.close()
    return render_template('reset.html')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=80, debug=True)
    # print(mapdisplay())