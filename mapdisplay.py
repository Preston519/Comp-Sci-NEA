from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=''):
    return render_template('hello.html', name=name)

@app.route('/maps')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=80, debug=True)