# Serve data from JSON API

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def json():
    marks = {
        "dushyant": 60,
        "mayank": 70,
        "ram": 50,
        "amit": 30,
        "krish": 40
    }
    values = ["Starting" , marks ,"Ending"]
    # I want to expose this json as an API how we can do this ? use jsonify

    return jsonify(values)

app.run(debug=True)

# Now you run this it will show json file on the browser
# This result file is an proper json you can check it in inspect
# You can also jsonify the list