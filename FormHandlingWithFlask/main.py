from flask import Flask , request ,render_template

app = Flask(__name__)

@app.route("/" , methods=["GET", "POST"])
def hello_world():

    # print(request.method)
    # print(request.form)

    if(request.method == "POST"):
        # Handle the form 
        if request.method == "POST":
            with open("file.txt", "w") as f:
                f.write(f"The mail is {request.form['email']} and password is {request.form['password']}")
            return "Form submitted successfully!"

    
    else:
        return render_template("contact.html")
    
app.run(debug=True)