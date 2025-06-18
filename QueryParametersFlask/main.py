from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def hello_world():
    # name = "Dushyant"
    # token = 67000

    # name = request.args['name']
    # token = request.args['tokens']   # Now url working properly now give default value by name , token variable



    name = "Dushyant"
    token = 67000

    if "name" in request.args.keys():
        name = request.args['name']           # if spelling of name is correct then it show only given name with default tokens
    
    if "tokens" in request.args.keys():       # if spelling of token is correct then it show only given tokens with default name 
        token = request.args['tokens']         # Now url still works after the loading 

    return render_template("index.html", name = name , token = token)

app.run(debug=True) 