from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import os

app = Flask(__name__)

# MySQL configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

def init_db():
    if not os.path.exists('test.db'):
        conn = sqlite3.connect('test.db')
        with open('init.sql', 'r') as f:
            schema = f.read()
            conn.executescript(schema)
        conn.close()

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


@app.route("/", methods=["GET"])
def index():
    name = request.args.get('name')
    error = None
    results = None
    if name:
        try:
            query = f"SELECT * FROM users WHERE username = '{name}'"
            results = db.engine.execute(query) # This is vulnerable to SQL injection
        except Exception as e:
            error = str(e)

    return render_template("index.html", results=results, error=error)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=8000)

