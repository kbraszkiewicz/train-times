from flask import Flask
from flask import render_template
from dataclasses import dataclass


app = Flask(__name__, static_folder='static')

@dataclass
class Train:
    departue_station: str
    final_station:str
    due_time:str
    status:str
    platform:str
    stops:str

@dataclass
class Board:
    station:str
    trains:[Train]


@app.route("/")
def hello():
    return render_template("template.html")


@app.route("/login")
def login():
    return "Login Page!"


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=80, debug=1)