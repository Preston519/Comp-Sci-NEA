from graphing import *
import numpy as np
import copy

distances = create_graph()

def nearestneighbour(graph, max_capacity = 20):
    num_points = len(graph.graph)
    graphcopy = copy.deepcopy(graph.graph)
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
    while len(route) < num_points:
        # graphcopy[current]: dict
        # print(graphcopy)
        # print(graphcopy[current])
        for point in graphcopy:
            if current in graphcopy[point]:
                graphcopy[point].pop(current)
        nearest = min(graphcopy[current], key=graphcopy[current].get)
        graphcopy.pop(current)
        route.append(nearest)
        current = nearest
        # nearest = None
        # min_dist = float("inf")
    route.append("Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ")
    return route

nn_route = nearestneighbour(distances)
print(nn_route)
print(distances.calc_distance(nn_route))