# Jinga template engine
# Link for Jinga template -> https://flask.palletsprojects.com/en/stable/templating/   (jinga template flask)

# Flask use jinga 2 as a template engine
# One simple usecase of jinga template is pass a variable to a template 

# This is the easiest way to pass a variable into template(By Flask)

# Extension for jinga -> Jinja Snippets flask

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
    return render_template("index.html", marks = marks)

app.run(debug=True)