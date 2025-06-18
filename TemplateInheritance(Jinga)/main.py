# Use this for reference  ->  https://flask.palletsprojects.com/en/stable/patterns/templateinheritance/

# To use the inheritance we make a base template from which all my other template will be inherited 

# I make the base page according to this we can adjust our content in all the three pages

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

app.run(debug=True)