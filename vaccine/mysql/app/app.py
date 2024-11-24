from flask import Flask, request, render_template
from flaskext.mysql import MySQL

app = Flask(__name__)

# MySQL configuration
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'test'
app.config['MYSQL_DATABASE_HOST'] = 'db'

mysql = MySQL(app)

@app.route("/", methods=["GET"])
def index():
    name = request.args.get('name')
    error = None
    results = None
    if name:
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            query = f"SELECT * FROM users WHERE username = '{name}'"
            cursor.execute(query)
            results = cursor.fetchall()
            cursor.close()
            conn.close()
        except Exception as e:
            error = str(e)

    return render_template("index.html", results=results, error=error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

