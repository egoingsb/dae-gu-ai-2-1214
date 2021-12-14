from flask import Flask
import random
app = Flask(__name__)

@app.route("/")
def index():
    return "Home"

@app.route("/read/", defaults={'id': None})
@app.route("/read/<id>/")
def read(id):
    return "Read"

@app.route('/create/')
def create():
    return 'Create'


app.run(debug=True,host="0.0.0.0",port="8000")
