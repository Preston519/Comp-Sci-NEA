from finalised import Graph

# Constructive Heuristics

def nearestneighbour(graph: Graph, max_capacity = 20): # TODO: don't use deepcopy. Very space inefficient. Use visited list instead.
    # graphcopy = copy.deepcopy(graph.graph)
    # for point in graphcopy:
    #         if graph.depot in graphcopy[point]:
    #             graphcopy[point].pop(graph.depot)
    unvisited = graph.nodes
    unvisited.pop(0)
    # graphcopy: dict[dict]
    routes = []
    while len(unvisited) > 0:
        current = sorted(unvisited, key=graph.dist_graph[graph.depot].get)
        route = [current]
        while len(route) < max_capacity+1 and graph[current]:
            nearest = min(graphcopy[current], key=graphcopy[current].get)
            if current != graph.depot:
                graphcopy.pop(current)
            route.append(nearest)
            current = nearest
            for point in graphcopy:
                if current in graphcopy[point]:
                    graphcopy[point].pop(current)
        graphcopy.pop(current)
        route.append(graph.depot)
        routes.append(route)
    return routes

def sweep(graph, max_capacity=20):
    pass

def saving(graph: Graph, max_capacity=20): # The most well known VRP heuristic!
    graphcopy = copy.deepcopy(graph.graph)
    nodescopy = copy.deepcopy(graph.nodes)
    depot = graph.depot
    routes = list([node] for node in nodescopy)
    # print(routes)
    savings = generate_savings(graph)
    # print(savings)
    while savings:
        current = max(savings, key=savings.get)
        in_route, indexes = is_in_route(current, routes) # Ignore the pair if one or more of the nodes are already interior to a route, because a more optimal saving has already been made
        if is_interior(current[1], routes[indexes[1]]) or is_interior(current[0], routes[indexes[0]]) or any(len(routes[index]) >= max_capacity for index in indexes):
            savings.pop(current)
            continue
        if not in_route[0] and not in_route[1]: # If neither node is in an existing route
            routes.pop(routes.index([current[1]]))
            # print(routes)
            routes[routes.index([current[0]])].append(current[1])
        elif not in_route[0]: # If only one node is in an existing route, for both nodes
            if routes[indexes[1]].index(current[1]) == 0:
                routes[indexes[1]].insert(0, current[0])
            else:
                routes[indexes[1]].append(current[0])
            routes.pop(indexes[0])
        elif not in_route[1]:
            if routes[indexes[0]].index(current[0]) == 0:
                routes[indexes[0]].insert(0, current[1])
            else:
                routes[indexes[0]].append(current[1])
            routes.pop(indexes[1])
        elif not(indexes[0] == indexes[1]): # If both nodes are in two different existing routes
            routes[indexes[0]] = merge(routes[indexes[0]], routes[indexes[1]], current)
            routes.pop(indexes[1])
        savings.pop(current)
    for route in routes:
        route.insert(0, depot)
        route.append(depot)
    return routes

def merge(route0, route1, link):
    if route0.index(link[0]) != len(route0)-1:
        route0.reverse()
    if route1.index(link[1]) != len(route1)-1:
        route1.reverse()
    merged_route = route0 + route1
    if distances.calc_distance(merged_route) > distances.calc_distance(list(reversed(merged_route))):
        merged_route.reverse()
    return merged_route

def is_interior(point: tuple, route: list):
    index = route.index(point)
    return not(index == 0 or index == len(route)-1)
        
def is_in_route(pair: tuple, routes: list):
    in_route = [False, False]
    indexes = [None, None]
    for num in range(2):
        for route in routes:
            if pair[num] in route:
                indexes[num] = routes.index(route)
                if len(route) > 1:
                    in_route[num] = True
    return in_route, indexes

def generate_savings(graph: Graph):
    savings = dict()
    nodescopy = graph.nodes
    # nodescopy.pop(graph.nodes.index(graph.depot))
    print(nodescopy)
    for nodenum in range(len(nodescopy)):
        for node2 in nodescopy[nodenum+1:]:
            # if routes[routenum] != route2: # Should never be equal?
            # print((nodenum, node2))
            savings[(nodescopy[nodenum], node2)] = graph.graph[nodescopy[nodenum]][graph.depot] + graph.graph[graph.depot][node2] - graph.graph[nodescopy[nodenum]][node2]
            # print(nodenum)
    return savings



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