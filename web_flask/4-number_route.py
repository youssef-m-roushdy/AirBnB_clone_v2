#!/usr/bin/python3
""" 4. Script to start a Flask web application Is it a number?"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>',  strict_slashes=False)
def c(text):
    return 'C {}'.format(text.replace("_", " "))


@app.route('/python/',  strict_slashes=False)
@app.route('/python/<text>',  strict_slashes=False)
def python(text="is cool"):
    return 'Python {}'.format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def check_number(n):
    return f"{n} is a number"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
