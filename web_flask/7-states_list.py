#!/usr/bin/python3
""" script that starts a Flask web application """
from models import storage
from flask import Flask, render_template
from models.state import State
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """ list all states"""
    states = list(storage.all(State).values())
    states.sort(key=lambda state: state.name)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exception):
    ''''closes the connection'''
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
