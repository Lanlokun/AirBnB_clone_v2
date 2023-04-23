#!/usr/bin/python3
""" Script that starts a Flask web application that displays a list of states """

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext()
def teardown_db(exception):
    """ Function that closes the database """
    storage.close()

@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Function that returns a list of states """
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)
