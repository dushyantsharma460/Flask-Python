from flask import Flask,render_template

app = Flask(__name__)

# All the file that you want to use them to user will be putted inside static folder 

# Does user can access main.py with brownser ?   -> No (Security concern)

@app.route("/")
def hello_world():
    return render_template("index.html")

app.run(port=9000, debug=True, host="dushyantfile")