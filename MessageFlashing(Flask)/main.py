from flask import Flask, flash, render_template

# Messaging flashing is used to show temporary messaging to user in flask
# What use of this ? some time user log out then to confirm to user we show temporary message to user

app = Flask(__name__)

# Flashing works only if you have a secret key in your flask application
app.secret_key = "3h4i3hu564h6uu3u3gjcc"
# Message flashing in flask works based on session will have to make sure a super secret key present


@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/logout")
def logout():
    flash("You have logged out !", "success")
    return render_template("index.html")

app.run(debug=True)
