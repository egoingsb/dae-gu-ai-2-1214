from flask import Flask
import random
app = Flask(__name__)

@app.route("/")
def index():
    return """
    <html>
    <body>
            <h1><a href="/index.html">web</a></h1>
            <ul>
                <li><a href="/1.html">html</a></li>
                <li><a href="/2.html">css</a></li>
                <li><a href="/3.html">js</a></li>
            </ul>
            <h2>Welcome</h2>
            Hello, WEB
        </body>
    </html>
    """

@app.route("/read/", defaults={'id': None})
@app.route("/read/<id>/")
def read(id):
    return "Read"

@app.route('/create/')
def create():
    return 'Create'


app.run(debug=True,host="0.0.0.0",port="8000")
