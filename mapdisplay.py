from flask import Flask, request, render_template

app = Flask(__name__)

sav_routes = [['Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ', '20 Parsons Mead, Abingdon, Oxfordshire', '8 Morgan Vale, Abingdon, Oxfordshire', 'Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ'], ['Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ', 'Taldysai Village, Kazakhstan', '1 Hollow Way, Oxford, OX4 2LZ', 'Ashmolean Museum, Beaumont Street, Oxfordshire', '16 Acacia Gardens, Southmoor, Abingdon OX13 5DE', '25 The Park, Cumnor, Oxford OX2 9QS', 'Abingdon School, Faringdon Lodge, Abingdon OX14 1BQ']]

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

@app.route('/maps')
def mapdisplay(maps=[]):
    embeds = routes_to_embed(sav_routes)
    print(embeds)
    return render_template('mapdisplay.html', embeds=embeds)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=80, debug=True)