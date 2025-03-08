from final_heuristics import Savings, Interchange, TwoOpt
from finalised import Graph

graph = Graph(nodes=['John Mason School, Wootton Rd, Abingdon'], depot='Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ')

graph.create_graph()
print(graph.dist_graph)
print(graph.time_graph)
print()

input()

graph1 = Graph(nodes=['St. Helens Church, St Helens Ct, Abingdon', 'Nags Head, The Bridge, Abingdon'], depot='Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ')

graph1.create_graph()
print(graph1.dist_graph)
print(graph1.time_graph)
print()

input()

# A premade graph with the time and distance graphs all set
testgraph = Graph(time_graph={'8 Farriers Mews, Abingdon, Oxfordshire': {'1 Hollow Way, Oxford, OX4 2LZ': 1003, '8 Morgan Vale, Abingdon, Oxfordshire': 418, '20 Parsons Mead, Abingdon, Oxfordshire': 402, '25 The Park, Cumnor, Oxford OX2 9QS': 907, '16 Acacia Gardens, Southmoor, Abingdon OX13 5DE': 1138, 'Taldysai Village, Kazakhstan': 242482, 'Ashmolean Museum, Beaumont Street, Oxfordshire': 1186, 'Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ': 351}, '1 Hollow Way, Oxford, OX4 2LZ': {'8 Farriers Mews, Abingdon, Oxfordshire': 959, '8 Morgan Vale, Abingdon, Oxfordshire': 957, '20 Parsons Mead, Abingdon, Oxfordshire': 884, '25 The Park, Cumnor, Oxford OX2 9QS': 1001, '16 Acacia Gardens, Southmoor, Abingdon OX13 5DE': 1539, 'Taldysai Village, Kazakhstan': 241837, 'Ashmolean Museum, Beaumont Street, Oxfordshire': 1059, 'Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ': 1028}, '8 Morgan Vale, Abingdon, Oxfordshire': {'8 Farriers Mews, Abingdon, Oxfordshire': 375, '1 Hollow Way, Oxford, OX4 2LZ': 994, '20 Parsons Mead, Abingdon, Oxfordshire': 142, '25 The Park, Cumnor, Oxford OX2 9QS': 574, '16 Acacia Gardens, Southmoor, Abingdon OX13 5DE': 920, 'Taldysai Village, Kazakhstan': 242477, 'Ashmolean Museum, Beaumont Street, Oxfordshire': 1177, 'Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ': 234}, '20 Parsons Mead, Abingdon, Oxfordshire': {'8 Farriers Mews, Abingdon, Oxfordshire': 354, '1 Hollow Way, Oxford, OX4 2LZ': 921, '8 Morgan Vale, Abingdon, Oxfordshire': 141, '25 The Park, Cumnor, Oxford OX2 9QS': 630, '16 Acacia Gardens, Southmoor, Abingdon OX13 5DE': 976, 'Taldysai Village, Kazakhstan': 242404, 'Ashmolean Museum, Beaumont Street, Oxfordshire': 1104, 'Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ': 212}, '25 The Park, Cumnor, Oxford OX2 9QS': {'8 Farriers Mews, Abingdon, Oxfordshire': 879, '1 Hollow Way, Oxford, OX4 2LZ': 984, '8 Morgan Vale, Abingdon, Oxfordshire': 592, '20 Parsons Mead, Abingdon, Oxfordshire': 645, '16 Acacia Gardens, Southmoor, Abingdon OX13 5DE': 704, 'Taldysai Village, Kazakhstan': 242418, 'Ashmolean Museum, Beaumont Street, Oxfordshire': 1152, 'Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ': 737}, '16 Acacia Gardens, Southmoor, Abingdon OX13 5DE': {'8 Farriers Mews, Abingdon, Oxfordshire': 1133, '1 Hollow Way, Oxford, OX4 2LZ': 1510, '8 Morgan Vale, Abingdon, Oxfordshire': 952, '20 Parsons Mead, Abingdon, Oxfordshire': 1005, '25 The Park, Cumnor, Oxford OX2 9QS': 694, 'Taldysai Village, Kazakhstan': 242944, 'Ashmolean Museum, Beaumont Street, Oxfordshire': 1678, 'Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ': 888}, 'Taldysai Village, Kazakhstan': {'8 Farriers Mews, Abingdon, Oxfordshire': 243428, '1 Hollow Way, Oxford, OX4 2LZ': 242827, '8 Morgan Vale, Abingdon, Oxfordshire': 243426, '20 Parsons Mead, Abingdon, Oxfordshire': 243353, '25 The Park, Cumnor, Oxford OX2 9QS': 243468, '16 Acacia Gardens, Southmoor, Abingdon OX13 5DE': 244008, 'Ashmolean Museum, Beaumont Street, Oxfordshire': 243182, 'Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ': 243533}, 'Ashmolean Museum, Beaumont Street, Oxfordshire': {'8 Farriers Mews, Abingdon, Oxfordshire': 1187, '1 Hollow Way, Oxford, OX4 2LZ': 1041, '8 Morgan Vale, Abingdon, Oxfordshire': 1185, '20 Parsons Mead, Abingdon, Oxfordshire': 1112, '25 The Park, Cumnor, Oxford OX2 9QS': 1126, '16 Acacia Gardens, Southmoor, Abingdon OX13 5DE': 1613, 'Taldysai Village, Kazakhstan': 242249, 'Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ': 1256}, 'Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ': {'8 Farriers Mews, Abingdon, Oxfordshire': 190, '1 Hollow Way, Oxford, OX4 2LZ': 1091, '8 Morgan Vale, Abingdon, Oxfordshire': 243, '20 Parsons Mead, Abingdon, Oxfordshire': 238, '25 The Park, Cumnor, Oxford OX2 9QS': 731, '16 Acacia Gardens, Southmoor, Abingdon OX13 5DE': 887, 'Taldysai Village, Kazakhstan': 242504, 'Ashmolean Museum, Beaumont Street, Oxfordshire': 1274}}, dist_graph={'8 Farriers Mews, Abingdon, Oxfordshire': {'1 Hollow Way, Oxford, OX4 2LZ': 12054, '8 Morgan Vale, Abingdon, Oxfordshire': 2959, '20 Parsons Mead, Abingdon, Oxfordshire': 3765, '25 The Park, Cumnor, Oxford OX2 9QS': 9055, '16 Acacia Gardens, Southmoor, Abingdon OX13 5DE': 11807, 'Taldysai Village, Kazakhstan': 5782398, 'Ashmolean Museum, Beaumont Street, Oxfordshire': 11322, 'Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ': 1816}, '1 Hollow Way, Oxford, OX4 2LZ': {'8 Farriers Mews, Abingdon, Oxfordshire': 11812, '8 Morgan Vale, Abingdon, Oxfordshire': 12110, '20 Parsons Mead, Abingdon, Oxfordshire': 11556, '25 The Park, Cumnor, Oxford OX2 9QS': 14141, '16 Acacia Gardens, Southmoor, Abingdon OX13 5DE': 20554, 'Taldysai Village, Kazakhstan': 5775864, 'Ashmolean Museum, Beaumont Street, Oxfordshire': 6103, 'Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ': 12953}, '8 Morgan Vale, Abingdon, Oxfordshire': {'8 Farriers Mews, Abingdon, Oxfordshire': 2516, '1 Hollow Way, Oxford, OX4 2LZ': 12204, '20 Parsons Mead, Abingdon, Oxfordshire': 665, '25 The Park, Cumnor, Oxford OX2 9QS': 6355, '16 Acacia Gardens, Southmoor, Abingdon OX13 5DE': 13010, 'Taldysai Village, Kazakhstan': 5786916, 'Ashmolean Museum, Beaumont Street, Oxfordshire': 11472, 'Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ': 1571}, '20 Parsons Mead, Abingdon, Oxfordshire': {'8 Farriers Mews, Abingdon, Oxfordshire': 2513, '1 Hollow Way, Oxford, OX4 2LZ': 11710, '8 Morgan Vale, Abingdon, Oxfordshire': 726, '25 The Park, Cumnor, Oxford OX2 9QS': 6822, '16 Acacia Gardens, Southmoor, Abingdon OX13 5DE': 13476, 'Taldysai Village, Kazakhstan': 5786422, 'Ashmolean Museum, Beaumont Street, Oxfordshire': 10978, 'Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ': 1568}, '25 The Park, Cumnor, Oxford OX2 9QS': {'8 Farriers Mews, Abingdon, Oxfordshire': 8595, '1 Hollow Way, Oxford, OX4 2LZ': 13709, '8 Morgan Vale, Abingdon, Oxfordshire': 6338, '20 Parsons Mead, Abingdon, Oxfordshire': 6745, '16 Acacia Gardens, Southmoor, Abingdon OX13 5DE': 10841, 'Taldysai Village, Kazakhstan': 5788219, 'Ashmolean Museum, Beaumont Street, Oxfordshire': 14095, 'Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ': 7650}, '16 Acacia Gardens, Southmoor, Abingdon OX13 5DE': {'8 Farriers Mews, Abingdon, Oxfordshire': 11838, '1 Hollow Way, Oxford, OX4 2LZ': 23881, '8 Morgan Vale, Abingdon, Oxfordshire': 13075, '20 Parsons Mead, Abingdon, Oxfordshire': 13481, '25 The Park, Cumnor, Oxford OX2 9QS': 10764, 'Taldysai Village, Kazakhstan': 5798392, 'Ashmolean Museum, Beaumont Street, Oxfordshire': 24267, 'Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ': 11504}, 'Taldysai Village, Kazakhstan': {'8 Farriers Mews, Abingdon, Oxfordshire': 5792710, '1 Hollow Way, Oxford, OX4 2LZ': 5782149, '8 Morgan Vale, Abingdon, Oxfordshire': 5793008, '20 Parsons Mead, Abingdon, Oxfordshire': 5792454, '25 The Park, Cumnor, Oxford OX2 9QS': 5794946, '16 Acacia Gardens, Southmoor, Abingdon OX13 5DE': 5801452, 'Ashmolean Museum, Beaumont Street, Oxfordshire': 5786073, 'Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ': 5789026}, 'Ashmolean Museum, Beaumont Street, Oxfordshire': {'8 Farriers Mews, Abingdon, Oxfordshire': 11384, '1 Hollow Way, Oxford, OX4 2LZ': 6693, '8 Morgan Vale, Abingdon, Oxfordshire': 11683, '20 Parsons Mead, Abingdon, Oxfordshire': 11128, '25 The Park, Cumnor, Oxford OX2 9QS': 14341, '16 Acacia Gardens, Southmoor, Abingdon OX13 5DE': 24111, 'Taldysai Village, Kazakhstan': 5781397, 'Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ': 12525}, 'Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ': {'8 Farriers Mews, Abingdon, Oxfordshire': 1254, '1 Hollow Way, Oxford, OX4 2LZ': 13174, '8 Morgan Vale, Abingdon, Oxfordshire': 1585, '20 Parsons Mead, Abingdon, Oxfordshire': 1635, '25 The Park, Cumnor, Oxford OX2 9QS': 7682, '16 Acacia Gardens, Southmoor, Abingdon OX13 5DE': 11417, 'Taldysai Village, Kazakhstan': 5782625, 'Ashmolean Museum, Beaumont Street, Oxfordshire': 12442}}, nodes=['8 Farriers Mews, Abingdon, Oxfordshire', '1 Hollow Way, Oxford, OX4 2LZ', '8 Morgan Vale, Abingdon, Oxfordshire', '20 Parsons Mead, Abingdon, Oxfordshire', '25 The Park, Cumnor, Oxford OX2 9QS', '16 Acacia Gardens, Southmoor, Abingdon OX13 5DE', 'Taldysai Village, Kazakhstan', 'Ashmolean Museum, Beaumont Street, Oxfordshire'], depot='Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ')
test = Savings(testgraph, "distance", 30000)
test.execute()
for route in test.get_routes():
    print(f'{route} - Distance: {testgraph.calc_distance(route)}')
print()

input()
    
test1 = Savings(testgraph, "time", 50) # Time is in minutes
test1.execute()
for route in test1.get_routes():
    print(f'{route} - Time: {testgraph.calc_time(route)/60}')
print()

input()

test2 = Savings(testgraph, "capacity", 3)
test2.execute()
for route in test2.get_routes():
    print(f'{route} - Capacity: {len(route)}, Distance: {testgraph.calc_distance(route)}')
print()

input()

route1 = ["John Mason School, Wootton Rd, Abingdon OX14 1JB", "FitzHarris Castle Mound, Clifton Dr, Abingdon OX14 1ET", "St Nicolas C Of E Primary School, Boxhill Walk, Abingdon OX14 1HB", "Fitzharry House, Fitzharry's Rd, Abingdon OX14 1ER"]
graph = Graph(nodes = ["John Mason School, Wootton Rd, Abingdon OX14 1JB", "St Nicolas C Of E Primary School, Boxhill Walk, Abingdon OX14 1HB", "FitzHarris Castle Mound, Clifton Dr, Abingdon OX14 1ET", "Fitzharry House, Fitzharry's Rd, Abingdon OX14 1ER"], depot="Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ")
graph.create_graph()

twoopt = TwoOpt(graph, "distance", 3000, [route1])
twoopt.execute()

print(f'{route1} - Distance: {graph.calc_distance(route1)}')
new_route = twoopt.get_routes()[0]
print(f'{new_route} - Distance: {graph.calc_distance(new_route)}')

twoopt = TwoOpt(graph, "time", 3000, [route1])
twoopt.execute()

print(f'{route1} - Time: {graph.calc_time(route1)}')
new_route = twoopt.get_routes()[0]
print(f'{new_route} - Time: {graph.calc_time(new_route)}')
print()

input()

routes = [["John Mason School, Wootton Rd, Abingdon OX14 1JB", "FitzHarris Castle Mound, Clifton Dr, Abingdon OX14 1ET"], ["St Nicolas C Of E Primary School, Boxhill Walk, Abingdon OX14 1HB", "Fitzharry House, Fitzharry's Rd, Abingdon OX14 1ER"]]

for route in routes:
    print(f'{route} - Distance: {graph.calc_distance(route)}')
interchange = Interchange(graph, "distance", 2500, routes)
interchange.execute()
print()
for route in interchange.get_routes():
    print(f'{route} - Distance: {graph.calc_distance(route)}')
print()