# Flask Framework Project

This is a basic project using the Flask framework in Python.

## 📌 What is Flask?

Flask is a lightweight WSGI web application framework in Python. It is simple, flexible, and widely used for building web apps and APIs.

## 🚀 Getting Started

### 1. Install Flask

Make sure Python is installed. Then install Flask using pip:

```bash
pip install flask
2. Create Project Files
bash
Copy
Edit
project/
├── app.py
├── templates/
│   └── index.html
└── static/
    └── style.css
3. Example app.py
python
Copy
Edit
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
4. Run the App
bash
Copy
Edit
python app.py
Open your browser and go to:
http://127.0.0.1:5000

🔧 Features
Simple routing

Template rendering (Jinja2)

Static file support

Easy to extend

🧠 Useful Flask Commands
bash
Copy
Edit
flask run            # Run the server
flask --app app run  # Specify file (if not app.py)
📚 Learn More
Flask Documentation

Jinja Templating

Happy coding with Flask! 🔥

vbnet
Copy
Edit

Let me know if you want this version in Hindi or with GitHub deployment steps.
