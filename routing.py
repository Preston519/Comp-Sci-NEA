from graphing import *
import numpy as np
import copy

max_cap = int(input("Enter the maximum capacity of one bus: "))
distances = create_graph()
num_points = len(distances.graph)

# Constructive Heuristics

def nearestneighbour(graph: Graph, max_capacity = 20):
    graphcopy = copy.deepcopy(graph.graph)
    for point in graphcopy:
            if "Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ" in graphcopy[point]:
                graphcopy[point].pop("Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ")
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
    # capacity = max_capacity
    routes = []
    while len(graphcopy) > 1:
        current = "Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ"
        route = [current]
        while len(route) < max_capacity+1 and graphcopy[current]:
            # graphcopy[current]: dict
            # print(graphcopy)
            # print(graphcopy[current])
            # for point in graphcopy:
            #     if current in graphcopy[point]:
            #         graphcopy[point].pop(current)
            # print(graphcopy[current])
            nearest = min(graphcopy[current], key=graphcopy[current].get)
            if current != "Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ":
                graphcopy.pop(current)
            route.append(nearest)
            current = nearest
            for point in graphcopy:
                if current in graphcopy[point]:
                    graphcopy[point].pop(current)
            # nearest = None
            # min_dist = float("inf")
            # print(route)
        print(route)
        print(graphcopy)
        graphcopy.pop(current)
        route.append("Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ")
        routes.append(route)
    # print(graphcopy)
    return routes

def sweep(graph, max_capacity=20):
    pass

def savings(graph, max_capacity=20):
    pass


# Improvement Heuristics

def two_opt_swap(route: list, first: int, second: int):
    new_route = [None]*len(route)
    new_route[:first+1] = route[:first+1]
    new_route[second:] = route[second:]
    # print("dd")
    # print(new_route)
    new_route[first+1:second] = reversed(route[first+1:second])
    # new_route = list()
    # new_route.append(route[:first+1])
    # new_route.append(reversed)
    # print(new_route)
    # print(first, second)
    return new_route

def two_opt(graph: Graph, route: list): # Input route should always start and end with Abingdon School
    new_distance = float('inf')
    best_distance = graph.calc_distance(route)
    current_route = route
    for i in range(len(route[1:-2])):
        for j in range(len(route[i+1:-1])):
            new_route = two_opt_swap(current_route, i+1, j+i+2)
            # print(new_route)
            new_distance = graph.calc_distance(new_route)
            if new_distance < best_distance:
                current_route = new_route
                best_distance = new_distance
    return new_route

nn_route = nearestneighbour(distances, max_cap)
print(nn_route)
for route in nn_route:
    print(distances.calc_distance(route))
    # print(two_opt(distances, route))