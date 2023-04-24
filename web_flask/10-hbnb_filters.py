#!/usr/bin/python3
""" Script that starts a Flask web application loads states and cities and filters them """ 

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """ returns a list of states and cities """

    states = storage.all(State).values()
    cities = storage.all(City).values()
    return render_template('10-hbnb_filters.html', states=states, cities=cities)


@app.teardown_appcontext
def teardown_db(exception):
    """ closes the current SQLAlchemy Session """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)