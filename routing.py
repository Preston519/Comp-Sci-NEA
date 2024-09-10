from graphing import *
import numpy as np
import copy

distances = create_graph()

def nearestneighbour(graph, max_capacity = 20):
    # num_points = len(graph)
    graphcopy = copy.deepcopy(graph)
    graphcopy: dict[dict]
    # visited = np.zeros(num_points, dtype=bool)
    # routes = []
    # while np.sum(visited) < num_points:
    #     # current = 0
    #     current_capacity = 0
    #     route = [0]
    #     visited[0] = True
    #     while current_capacity < max_capacity:
    #         current = route[-1]
    #         nearest = None
    #         min_dist = float('inf')

    #         for neighbour in np.where(~visited)
    # visited = [False]*num_points
    current = "Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ"
    route = [current]
    while len(graphcopy) > 0:
        # graphcopy[current]: dict
        nearest = min(graphcopy[current], key=graphcopy[current].get)
        graphcopy.pop(current)
        route.append(nearest)
        current = nearest
        # nearest = None
        # min_dist = float("inf")
    return route
    
print(nearestneighbour(distances))