from flask import Flask
from flask import render_template

from liveData import getDepartureBoard
from data import Stop, Train, Board

app = Flask(__name__, static_folder='static')


@app.route("/")
def hello():
    train1 = Train("Leeds","HRS","19:45","On Time","6a","[stops]")
    train2 = Train("Leeds","HRS","19:45","On Time","6a","[stops]")
    board = Board("LDS",[train1,train2])
    return render_template("template.html",board=board)

@app.route("/station/<code>")
def station(code):
    print(code)

    train1 = Train("Leeds","HRS","19:45","On Time","6a","[stops]")
    train2 = Train("Leeds","HRS","19:45","On Time","6a","[stops]")
    board = Board("LDS",[train1,train2])
    return render_template("template.html",board=board)

@app.route("/station/live/<code>")
def stationLive(code):
    print(code)
    board = getDepartureBoard(code)
    return render_template("template.html",board=board)

@app.route("/login")
def login():
    return "Login Page!"


# if __name__ == "__main__":

#     app.run(host="0.0.0.0")