from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
#dekorátor

def hello():
    return render_template("index.html")

@app.route("/bye")
def bye():
    return render_template("bye.html")

@app.route("/form")
def form():
    name = request.args.get("name" , default="______")
    input_class = request.args.get("input_class", default="______")
    message = request.args.get("message", default="______")
    return render_template("form.html", name=name, input_class=input_class, message=message)

@app.route("/result")
def result():
    

if __name__ == "__main__":
    app.run(debug=True)