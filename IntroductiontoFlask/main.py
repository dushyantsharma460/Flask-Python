# use documentation to write the code 
# flask official docs ->  https://flask.palletsprojects.com/en/stable/
# flask minimal app -> https://flask.palletsprojects.com/en/stable/quickstart/

# Boiler plate code for the flask application -> take from above link (flask minimal app )

from flask import Flask , render_template    # we import a flask class from flask module
app = Flask(__name__)      # create new flask app

@app.route("/")
def hello_world(): 
    return render_template("index.html")

app.run(debug=True)  # i want to run this in debug mode means you show error on my html page.

# Usually this don't show error on the page 