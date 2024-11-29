from finalised import Graph

# testgraph = Graph(nodes=['Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ', '8 Farriers Mews, Abingdon, Oxfordshire', '1 Hollow Way, Oxford, OX4 2LZ', '8 Morgan Vale, Abingdon, Oxfordshire', '20 Parsons Mead, Abingdon, Oxfordshire', '25 The Park, Cumnor, Oxford OX2 9QS', '16 Acacia Gardens, Southmoor, Abingdon OX13 5DE', 'Taldysai Village, Kazakhstan', 'Ashmolean Museum, Beaumont Street, Oxfordshire'])
# testgraph.create_graph()

# All the parameters called graph are supposed to be Graph classes, but I can't do specify because importing Graph would be a circular import

# All works for Capacitated VRP

# Constructive Heuristics

class Heuristic:
    def __init__(self, graph: Graph, constraint, maximum):
        self._graph = graph
        self._constraint = constraint
        self._maximum = maximum
        self._routes = []

    def get_routes(self):
        return self._routes

class NearestNeighbour(Heuristic):
    def __init__(self, graph, constraint, maximum):
        super().__init__(graph, constraint, maximum)
    
    def execute(self):
        unvisited = self._graph.get_nodes()
        while len(unvisited) > 0:
            current = sorted(unvisited, key=self._graph.dist_graph[self._graph.depot].get)[0]
            route = [current]
            while len(route) < self._maximum and len(unvisited) > 1:
                unvisited.pop(unvisited.index(current))
                nearest = min(unvisited, key=self._graph.dist_graph[current].get)
                route.append(nearest)
                current = nearest
            unvisited.pop(unvisited.index(current))
            self._routes.append(route)


class Savings(Heuristic):
    def __init__(self, graph, constraint, maximum):
        super().__init__(self, graph, constraint, maximum)
        self._savings = dict()
    
    def execute(self):
        self._routes = list([node] for node in self._graph.nodes)
        self.generate_savings()
        while self._savings:
            current = max(self._savings, key=self._savings.get)
            in_route, indexes = self.is_in_route(current) # Ignore the pair if one or more of the nodes are already interior to a route, because a more optimal saving has already been made
            if not any(indexes):
                raise Exception("Indexes returned None")
            if self.is_interior(current, indexes) or self.check_constraint(indexes, current):
                self._savings.pop(current)
                continue
            if not any(in_route): # If neither node is in an existing route
                self._routes.pop(self._routes.index([current[1]]))
                self._routes[indexes[0]].append(current[1])
            else: # If one or both nodes are in an existing route
                self._routes[indexes[0]] = self.merge(indexes, current)
            self._savings.pop(current)
    
    def generate_savings(self):
        """Generates a dict of how much will be saved if two points are merged"""
        for nodenum, node1 in enumerate(self._graph.get_nodes()):
            for node2 in self._graph.get_nodes()[nodenum+1:]:
                self._savings[(node1, node2)] = self._graph.dist_graph[node1][self._graph.depot] + self._graph.dist_graph[self._graph.depot][node2] - self._graph.dist_graph[node1][node2]

    def is_in_route(self, pair: tuple):
        in_route = [False, False]
        indexes = [None, None]
        for num in range(2):
            for route in self._routes:
                if pair[num] in route:
                    indexes[num] = self._routes.index(route)
                    if len(route) > 1:
                        in_route[num] = True
        return in_route, indexes
    
    def is_interior(self, pair: tuple, indexes: list):
        """Returns True if one point is interior to a route"""
        for i in range(2):
            if 0 > self._routes[indexes[i]].index(pair[i]) > len(self._routes[indexes[i]])-1:
                return True
        return False
    
    def check_constraint(self, indexes: list, current: tuple):
        """Returns True if constraints are breached"""
        if self._constraint == "vehicles":
            return len(self._routes[indexes[0]]) + len(self._routes[indexes[1]]) > self._maximum
        elif self._constraint == "time":
            return self._graph.calc_time(self._routes[indexes[0]]) + self._graph.calc_time(self._routes[indexes[1]]) - self._savings[current] > self._maximum
        elif self._constraint == "distance":
            return self._graph.calc_distance(self._routes[indexes[0]]) + self._graph.calc_distance(self._routes[indexes[1]]) - self._savings[current] > self._maximum
        else:
            raise Exception("Invalid constraint")
        
    def merge(self, indexes: list, link: tuple):
        """Merges two routes together as part of saving method"""
        route0 = self._routes[indexes[0]] # Assigning temporary variables so as to not modify original routes
        route1 = self._routes[indexes[1]]
        if route0.index(link[0]) != len(route0)-1:
            route0.reverse()
        if route1.index(link[1]) != 0:
            route1.reverse()
        merged_route = route0 + route1
        if self._constraint == "time" and self._graph.calc_time(merged_route) > self._graph.calc_time(list(reversed(merged_route))):
            merged_route.reverse()
        elif self._constraint != "time" and self._graph.calc_distance(merged_route) > self._graph.calc_distance(list(reversed(merged_route))):
            merged_route.reverse()
        return merged_route
    
# Improvement Heuristics

class TwoOpt(Heuristic):
    def __init__(self, graph, constraint, maximum, routes):
        super().__init__(graph, constraint, maximum)
        self._routes = routes
    
    def execute(self):
        for num, route in enumerate(self._routes):
            new_distance = float('inf')
            best_distance = self._graph.calc_time(route) if self._constraint == "time" else self._graph.calc_distance(route)
            current_route = route
            for i in range(len(route[1:-2])):
                for j in range(len(route[i+1:-1])):
                    new_route = self.swap(num, i+1, j+i+2)
                    new_distance = self._graph.calc_time(route) if self._constraint == "time" else self._graph.calc_distance(route)
                    if new_distance < best_distance:
                        current_route = new_route
                        best_distance = new_distance
            self._routes[num] = current_route
    
    def swap(self, listIndex: int, first: int, second: int):
        """Swaps the points at indexes first and second in the route"""
        if first == second:
            return self._routes[listIndex]
        return self._routes[listIndex][:first+1] + list(reversed(self._routes[listIndex][first+1:second])) + self._routes[listIndex][second:]