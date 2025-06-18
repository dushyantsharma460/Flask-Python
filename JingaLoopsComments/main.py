from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    marks = {
        "John": 45,
        "Saurabh": 99,
        "Ansh": 55,
        "Alexa": 90,
        "Lily": 100
    }
    return render_template("jinga.html", marks = marks)

app.run(debug=True)