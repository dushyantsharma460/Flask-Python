# You can also change the static file url path as you want 
# I can access my static file like this:- http://127.0.0.1:5000/static/style.css
# But now I change the url of access by using flask url for 

from flask import Flask, render_template

# Create Flask app and change default static URL path from '/static' to '/assets'

# This is how you change static url path
# app = Flask(__name__, static_url_path="/public")    # Now you can access the file of static with public/file.exe


# This is how you can change static folder location

# From this the static folder name is change to assets your static folder file no longer accessable 
# Now your static folder is assets you can access all the files of assets not the static
# app = Flask(__name__, static_folder="assets")     # While using static_folder not use / at the end
# By this line we will not able to access things of main static folder things like style.css
# You can access only ->  http://127.0.0.1:5000/assets/anotherStyle.css


# Now from this line we will access only assets folder things with the name of static not assets
# app = Flask(__name__, static_folder="assets", static_url_path="/static")  


# Now it auto change in browser according to static_url_path

app = Flask(__name__, static_folder="assets", static_url_path="/public")  

# Route for root URL
@app.route("/")
def hello_world():
    return render_template("index.html")

# Run the app in debug mode
app.run(debug=True)
