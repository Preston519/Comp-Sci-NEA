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

def main():
    while True:
        sortparam = input("Make routes based on (D)istance or (T)ime?").upper()
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
    nodes = list(map(lambda x: x[0], response.fetchall()))
    address_map = Graph()
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
    print(address_map.graph)

if __name__ == "__main__":
    main()