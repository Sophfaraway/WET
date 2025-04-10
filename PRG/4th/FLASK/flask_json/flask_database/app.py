import sqlite3, random
from flask import Flask, render_template, request, redirect, url_for, g
import json

app = Flask(__name__)

DATABASE = "instance/database.db"

def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db
    
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource("schema.sql", mode="r") as file:
            db.cursor().executescript(file.read())
        db.commit()

@app.teardown_appcontext 
def close_connection(exception):
    db = get_db()
    if db is not None:
        db.close()

@app.route("/")
#dekorátor

def hello():
    return render_template("index.html")

@app.route("/bye")
def bye():
    return render_template("bye.html")

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form.get("name" )
        input_class = request.form.get("input_class")
        message = request.form.get("message")
        grade = random.randint(1,5)

        if len(input_class) > 4:
            input_class = "error"

        if len(input_class) > 4:
            print("error")

        # if name.isspace() == True:
        #     name.title()

        if ' ' in name:
            name = name.title()
        else:
            print("error 2")
            name = "error"
            

        cursor = get_db().cursor()
        cursor.execute(
            f"INSERT INTO students (student_name, class, student_message, grade) VALUES (?, ?, ?, ?)", (name, input_class, message, grade)
        )
        # if name and message and input_class:
        #     return redirect(url_for("result",  name=name, input_class=input_class, message=message))
        get_db().commit()

        
        
    return render_template("form.html")

@app.route("/result")
def result():
    cursor = get_db().cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    return render_template("result_all.html",  rows = rows)
   

# @app.route("/result2")
# def result2():
#     cursor = get_db().cursor()
#     cursor.execute("SELECT * FROM students")
#     rows = cursor.fetchall()
#     print(rows)
#     return render_template("result_all.html",  name=rows [0][1], input_class = rows [0][2], message = rows [0][3])
#     # return rows [0][1]


if __name__ == "__main__":
    init_db()
    app.run(debug=True)