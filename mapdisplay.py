from flask import Flask, request, render_template
import sqlite3
# from routing import *

app = Flask(__name__)

sav_routes = [['Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ', '20 Parsons Mead, Abingdon, Oxfordshire', '8 Morgan Vale, Abingdon, Oxfordshire', 'Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ'], ['Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ', 'Taldysai Village, Kazakhstan', '1 Hollow Way, Oxford, OX4 2LZ', 'Ashmolean Museum, Beaumont Street, Oxfordshire', '16 Acacia Gardens, Southmoor, Abingdon OX13 5DE', '25 The Park, Cumnor, Oxford OX2 9QS', 'Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ']]

map_routes = [
    ['Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ', 'Ashmolean Museum, Beaumont Street, Oxfordshire', 'Taldysai Village, Kazakhstan', '1 Hollow Way, Oxford, OX4 2LZ', '16 Acacia Gardens, Southmoor, Abingdon OX13 5DE', '25 The Park, Cumnor, Oxford OX2 9QS', 'Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ'] ,
    ['Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ', '8 Farriers Mews, Abingdon, Oxfordshire', '8 Morgan Vale, Abingdon, Oxfordshire', '20 Parsons Mead, Abingdon, Oxfordshire', 'Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ']
]

def fetch_data():
    # routes = []
    connection = sqlite3.connect("student.db")
    cursor = connection.cursor()
    routes = [[None]] * len(cursor.execute("SELECT RouteID FROM routes").fetchall()-1)
    data = []
    # for routeID in range(len(cursor.execute("SELECT RouteID FROM routes").fetchall())-1):
    #     response = cursor.execute("SELECT Address FROM students WHERE RouteID = ? ORDER BY RouteOrder ASC", (routeID,))
    #     route = list(map(lambda x: x[0], response.fetchall()))
    #     response = cursor.execute("SELECT Distance FROM routes WHERE RouteID = ?")
    #     data.append((route, ))
    response = cursor.execute("SELECT RouteID, Address FROM students ORDER BY RouteID, RouteOrder").fetchall()
    for address in response:
        routes[address[0]].append(address[1])
    response = cursor.execute("SELECT Distance, Stops FROM routes WHERE RouteID != -1 ORDER BY RouteID").fetchall()
    for info in response:
        data.append(info)
    # Do the thing where the list is predeclared like an array and then you can assign via enumerated variable cool done
    return data

def routes_to_embed(routes: list = []):
    embeds = []
    for route in routes:
        for address in route:
            address: str
            formatted = address.replace(", ", ",").replace(" ", "+")
            route[route.index(address)] = formatted
        embeds.append(f"https://www.google.com/maps/embed/v1/directions?key=AIzaSyDE2qaxHADLeBQO1zLqfDIasLOalcHWHi0&origin={route[0]}&destination={route[-1]}&waypoints={'|'.join(route[1:-1])}")
    return embeds

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=''):
    return render_template('hello.html', name=name)

@app.route('/maps/')
def mapdisplay():
    # connection = sqlite3.connect("student.db")
    # cursor = connection.cursor()
    # cursor.execute
    data, embeds = fetch_data()
    embeds = routes_to_embed(embeds)
    # print(embeds)
    return render_template('mapdisplay.html', maps=embeds)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=80, debug=True)