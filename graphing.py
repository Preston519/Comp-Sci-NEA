import sqlite3
import googlemaps
import sys

class Graph:
    def __init__(self, graph: dict = {}):
        self.graph = graph

    def add_edge(self, node1, node2, weight): # A directed link from node1 to node2
        if node1 not in self.graph:
            self.graph[node1] = {}
        self.graph[node1][node2] = weight

while True:
    sortingmethod = input("Make routes based on (D)istance or (T)ime?").upper()
    if sortingmethod == "D":
        sortingmethod = 0
        break
    elif sortingmethod == "T":
        sortingmethod = 1
        break
gmaps = googlemaps.Client(key="AIzaSyDE2qaxHADLeBQO1zLqfDIasLOalcHWHi0")
# gmaps = googlemaps.Client(key="AIza") # Key that doesn't work
connection = sqlite3.connect("students.db")
cursor = connection.cursor()
response = cursor.execute("SELECT Address FROM addresses")
# cursor.execute("CREATE TABLE movie(title, year, score)")
# print(response.fetchall()[0][0])
nodes = map(lambda x: x[0], response.fetchall())
address_map = Graph()
for address in nodes:
    for address2 in nodes:
        if address == address2: continue
        try:
            distance = gmaps.direction(address, address2, mode="driving")["bounds"]["legs"]["departure_time"]["distance"]["value"]
        except googlemaps.exceptions.ApiError:
            print("Invalid address input")
            sys.exit()
        address_map.add_edge()