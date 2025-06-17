from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/github")
def github():
    return render_template("github.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/linkdin")
def linkdin():
    return render_template("linkdin.html")

if __name__ == "__main__":
    app.run(debug=True)