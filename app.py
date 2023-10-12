from flask import Flask
from flask import render_template

app = Flask(__name__, static_folder='static')


@app.route("/")
def hello():
    return render_template("template.html")


@app.route("/login")
def login():
    return "Login Page!"


# if __name__ == "__main__":

#     app.run(host="0.0.0.0")