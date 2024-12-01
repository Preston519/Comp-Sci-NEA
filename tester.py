# class Route:
#     def __init__(self, depot: str = "", route: list = [], distance: int = 0, time: int = 0):
#         self.depot = depot
#         self.route = route
#         self.distance = distance
#         self.time = time
#         self.stops = len(route)
    
#     def set_distance(self, distance: int):
#         self.distance = distance

#     def set_time(self, time: int):
#         self.time = time

#     def add_stop(self, stop):
#         self.route.append(stop)
#         self.stops += 1
    
#     def remove_stop(self, num):
#         self.route.pop(num)
#         self.stops -= 1

#     def find_stop(self, stop):


#         return self.route.index(stop)
# import sqlite3
# connection = sqlite3.connect("student.db")
# cursor = connection.cursor()
# routeAmt = len(cursor.execute("SELECT RouteID FROM routes").fetchall())-1
# response = cursor.execute("SELECT RouteID, Address, StudentID, Name FROM students ORDER BY RouteID, RouteOrder").fetchall()
# routes = [[] for _ in range(routeAmt)]
# for address in response:
#     routes[address[0]].append((address[2], address[3], address[1]))

# print(list([x[2] for x in y]for y in routes))

x = 2
print(x > 1*5)