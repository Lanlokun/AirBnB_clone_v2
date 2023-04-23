#!/usr/bin/python3
""" Script that starts a Flask web application with a number route """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ Function that returns Hello HBNB! """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Function that returns HBNB """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ Function that returns C <text> """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """ Function that returns Python <text> """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ Function that returns n is a number """
    return '{} is a number'.format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
