import googlemaps
from flask import Flask, request, render_template
# from fileinput import filename
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
        # return f"{distance//1000}km {distance%1000}m"
        return time
    
    def find_distance(self, address1, address2):
        return self.dist_graph[address1][address2]
    
    def find_time(self, address1, address2):
        return self.time_graph[address1][address2]
    
    def create_graph(self):
        gmaps = googlemaps.Client(key="AIzaSyDE2qaxHADLeBQO1zLqfDIasLOalcHWHi0")
        for address in self.nodes:
            for address2 in self.nodes:
                if address == address2: continue
                weight = gmaps.directions(address, address2, mode="driving")[0]["legs"][0]["distance"]["value"]
                self.add_dist_edge(address, address2, weight)
                weight = gmaps.directions(address, address2, mode="driving")[0]["legs"][0]["duration"]["value"]
                self.add_time_edge(address, address2, weight)
        self.nodes.pop(0)
        # self.nodes.pop(0) # Remove the first item, which should be the depot

class Route:
    def __init__(self, depot: str = "", route: list = [], distance: int = 0, time: int = 0):
        self.depot = depot
        self.route = route
        self.distance = distance
        self.time = time
        self.stops = len(route)
    
    def set_distance(self, distance: int):
        self.distance = distance

    def set_time(self, time: int):
        self.time = time

    def add_stop(self, stop):
        self.route.append(stop)
        self.stops += 1
    
    def remove_stop(self, num):
        self.route.pop(num)
        self.stops -= 1

    def find_stop(self, stop):
        return self.route.index(stop)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        depot = request.form["depot"]
        file = request.files["addresses"]
        file.save(file.filename)
        with open(file.filename) as addresses:
            csvreader = csv.reader(addresses)
            connection = sqlite3.connect("student.db")
            cursor = connection.cursor()
            cursor.executemany("INSERT INTO students(StudentID, Name, Address, Year, RouteID) VALUES(?, ?, ?, ?, -1)", list(csvreader))
            cursor.execute("INSERT INTO students(StudentID, Name, Address, Year, RouteID) VALUES(-1, Depot, ?, -1, -1)", (depot,))
            connection.commit()
        remove(file.filename)
        return render_template('finished.html')
    return render_template('index.html')

@app.route('/maps')
@app.route('/maps/')
def mapdisplay():
    graph = processing()
    raise NotImplementedError

def processing():
    connection = sqlite3.connect("student.db")
    cursor = connection.cursor()
    nodes = list(map(lambda x: x[0], cursor.execute("SELECT Address FROM students").fetchall()))
    depot = cursor.execute("SELECT Address FROM students WHERE StudentID = -1").fetchone()
    graph = Graph(nodes=nodes, depot=depot)
    graph.create_graph()
    return graph
    # raise NotImplementedError

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=80)
    # print(mapdisplay())