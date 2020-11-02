import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def home():
    return 'Home Page'

@app.route('/stats/array')
def api_arr():
    return "Post the array here"

