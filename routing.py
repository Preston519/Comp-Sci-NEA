from graphing import *
import numpy as np
import copy

max_cap = int(input("Enter the maximum capacity of one bus: "))
# distances = create_graph()
distances = Graph({'20 Parsons Mead, Abingdon, Oxfordshire': {'8 Morgan Vale, Abingdon, Oxfordshire': 726, 'Taldysai Village, Kazakhstan': 5882537, 'Ashmolean Museum, Beaumont Street, Oxfordshire': 10978, '1 Hollow Way, Oxford, OX4 2LZ': 11709, '25 The Park, Cumnor, Oxford OX2 9QS': 6823, '16 Acacia Gardens, Southmoor, Abingdon OX13 5DE': 13477, 'Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ': 1615}, '8 Morgan Vale, Abingdon, Oxfordshire': {'20 Parsons Mead, Abingdon, Oxfordshire': 665, 'Taldysai Village, Kazakhstan': 5883030, 'Ashmolean Museum, Beaumont Street, Oxfordshire': 11471, '1 Hollow Way, Oxford, OX4 2LZ': 12202, '25 The Park, Cumnor, Oxford OX2 9QS': 6355, '16 Acacia Gardens, Southmoor, Abingdon OX13 5DE': 13009, 'Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ': 1616}, 'Taldysai Village, Kazakhstan': {'20 Parsons Mead, Abingdon, Oxfordshire': 5807898, '8 Morgan Vale, Abingdon, Oxfordshire': 5808452, 'Ashmolean Museum, Beaumont Street, Oxfordshire': 5801517, '1 Hollow Way, Oxford, OX4 2LZ': 5797593, '25 The Park, Cumnor, Oxford OX2 9QS': 5810391, '16 Acacia Gardens, Southmoor, Abingdon OX13 5DE': 5820159, 'Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ': 5804516}, 'Ashmolean Museum, Beaumont Street, Oxfordshire': {'20 Parsons Mead, Abingdon, Oxfordshire': 11128, '8 Morgan Vale, Abingdon, Oxfordshire': 11682, 'Taldysai Village, Kazakhstan': 5877808, '1 Hollow Way, Oxford, OX4 2LZ': 6141, '25 The Park, Cumnor, Oxford OX2 9QS': 14342, '16 Acacia Gardens, Southmoor, Abingdon OX13 5DE': 24110, 'Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ': 12571}, '1 Hollow Way, Oxford, OX4 2LZ': {'20 Parsons Mead, Abingdon, Oxfordshire': 11556, '8 Morgan Vale, Abingdon, Oxfordshire': 12110, 'Taldysai Village, Kazakhstan': 5872304, 'Ashmolean Museum, Beaumont Street, Oxfordshire': 6102, '25 The Park, Cumnor, Oxford OX2 9QS': 13899, '16 Acacia Gardens, Southmoor, Abingdon OX13 5DE': 20553, 'Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ': 12999}, '25 The Park, Cumnor, Oxford OX2 9QS': {'20 Parsons Mead, Abingdon, Oxfordshire': 6746, '8 Morgan Vale, Abingdon, Oxfordshire': 6338, 'Taldysai Village, Kazakhstan': 5884538, 'Ashmolean Museum, Beaumont Street, Oxfordshire': 12979, '1 Hollow Way, Oxford, OX4 2LZ': 13710, '16 Acacia Gardens, Southmoor, Abingdon OX13 5DE': 10842, 'Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ': 7697}, '16 Acacia Gardens, Southmoor, Abingdon OX13 5DE': {'20 Parsons Mead, Abingdon, Oxfordshire': 13482, '8 Morgan Vale, Abingdon, Oxfordshire': 13075, 'Taldysai Village, Kazakhstan': 5894709, 'Ashmolean Museum, Beaumont Street, Oxfordshire': 23150, '1 Hollow Way, Oxford, OX4 2LZ': 23881, '25 The Park, Cumnor, Oxford OX2 9QS': 10765, 'Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ': 11206}, 'Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ': {'20 Parsons Mead, Abingdon, Oxfordshire': 1681, '8 Morgan Vale, Abingdon, Oxfordshire': 1630, 'Taldysai Village, Kazakhstan': 5878786, 'Ashmolean Museum, Beaumont Street, Oxfordshire': 12488, '1 Hollow Way, Oxford, OX4 2LZ': 13219, '25 The Park, Cumnor, Oxford OX2 9QS': 7728, '16 Acacia Gardens, Southmoor, Abingdon OX13 5DE': 11338}})
# To save on gmaps credit
num_points = len(distances.graph)



# Constructive Heuristics

def nearestneighbour(graph: Graph, max_capacity = 20):
    graphcopy = copy.deepcopy(graph.graph)
    for point in graphcopy:
            if "Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ" in graphcopy[point]:
                graphcopy[point].pop("Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ")
    graphcopy: dict[dict]
    routes = []
    while len(graphcopy) > 1:
        current = "Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ"
        route = [current]
        while len(route) < max_capacity+1 and graphcopy[current]:
            nearest = min(graphcopy[current], key=graphcopy[current].get)
            if current != "Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ":
                graphcopy.pop(current)
            route.append(nearest)
            current = nearest
            for point in graphcopy:
                if current in graphcopy[point]:
                    graphcopy[point].pop(current)
        graphcopy.pop(current)
        route.append("Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ")
        routes.append(route)
    return routes

def sweep(graph, max_capacity=20):
    pass

def savings(graph, max_capacity=20):
    pass


# Improvement Heuristics

def two_opt_swap(route: list, first: int, second: int):
    if first == second:
        return route
    new_route = [None]*len(route)
    new_route[:first+1] = route[:first+1]
    new_route[second:] = route[second:]
    new_route[first+1:second] = reversed(route[first+1:second])
    return new_route

def two_opt(graph: Graph, route: list): # Input route should always start and end with Abingdon School
    new_distance = float('inf')
    best_distance = graph.calc_distance(route)
    current_route = route
    for i in range(len(route[1:-2])):
        for j in range(len(route[i+1:-1])):
            new_route = two_opt_swap(current_route, i+1, j+i+2)
            new_distance = graph.calc_distance(new_route)
            if new_distance < best_distance:
                current_route = new_route
                best_distance = new_distance
    return current_route

nn_route = nearestneighbour(distances, max_cap)
for route in nn_route:
    print(route)
    print(distances.calc_distance(route))
    topt_route = two_opt(distances, route)
    print(topt_route)
    print(distances.calc_distance(topt_route))