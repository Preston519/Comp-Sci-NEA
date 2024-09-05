import sqlite3
import googlemaps

class Graph:
    def __init__(self, graph: dict = {}):
        self.graph = graph

    def add_edge(self, node1, node2, weight): # A directed link from node1 to node2
        if node1 not in self.graph:
            self.graph[node1] = {}
        self.graph[node1][node2] = weight

gmaps = googlemaps.Client(key="AIzaSyDE2qaxHADLeBQO1zLqfDIasLOalcHWHi0")
