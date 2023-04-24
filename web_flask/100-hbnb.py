#!/usr/bin/python3
""" Script that starts a Flask web application with a route that 
    returns a HTML page  that filters the states by a given tag:"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.city import City


app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ returns a list of states and cities """

    states = storage.all(State).values()
    cities = storage.all(City).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()
    return render_template('100-hbnb.html', states=states, cities=cities, amenities=amenities, places=places)


def teardown_db(exception):
    """ closes the current SQLAlchemy Session """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

    