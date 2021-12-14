from flask import Flask
import sqlite3
app = Flask(__name__)

@app.route("/")
def index():
    con = sqlite3.connect('data.db')
    cursor = con.cursor()
    cursor.execute('SELECT * FROM topics')
    rows = cursor.fetchall()
    liTag = ''
    for row in rows:
        liTag = liTag + f'<li><a href="/read/{row[0]}">{row[1]}</a></li>'
    return f"""
    <html>
    <body>
            <h1><a href="/index.html">web</a></h1>
            <ul>
                {liTag}
            </ul>
            <h2>Welcome</h2>
            Hello, WEB
        </body>
    </html>
    """

@app.route("/read/", defaults={'id': None})
@app.route("/read/<id>/")
def read(id):
    con = sqlite3.connect('data.db')
    cursor = con.cursor()
    cursor.execute('SELECT * FROM topics')
    rows = cursor.fetchall()
    liTag = ''
    for row in rows:
        liTag = liTag + f'<li><a href="/read/{row[0]}">{row[1]}</a></li>'

    cursor.execute('SELECT * FROM topics WHERE id = ?', (id,))
    topic = cursor.fetchone()
    return f"""
    <html>
    <body>
            <h1><a href="/index.html">web</a></h1>
            <ul>
                {liTag}
            </ul>
            <h2>{topic[1]}</h2>
            {topic[2]}
        </body>
    </html>
    """

@app.route('/create/')
def create():
    return 'Create'


app.run(debug=True,host="0.0.0.0",port="8000")
