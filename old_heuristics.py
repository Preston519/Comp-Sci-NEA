def nearestneighbour(graph, max_capacity = 5):
    unvisited = graph.get_nodes()
    routes = []
    while len(unvisited) > 0:
        current = sorted(unvisited, key=graph.dist_graph[graph.depot].get)[0]
        route = [current]
        while len(route) < max_capacity and len(unvisited) > 1:
            unvisited.pop(unvisited.index(current))
            nearest = min(unvisited, key=graph.dist_graph[current].get)
            route.append(nearest)
            current = nearest
        unvisited.pop(unvisited.index(current))
        routes.append(route)
    return routes