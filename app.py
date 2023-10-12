from flask import Flask
from flask import render_template
from dataclasses import dataclass
from flaskext.mysql import MySQL

from liveData import getDepartureBoard
from data import Stop, Train, Board

app = Flask(__name__, static_folder='static')

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'trains'
app.config['MYSQL_DATABASE_HOST'] = '192.168.1.106'
app.config['MYSQL_DATABASE_PORT'] = 3308
mysql.init_app(app)

@dataclass
class Stop:
    name:str
    arival_time:str

@dataclass
class Train:
    departue_station: str
    final_station:str
    due_time:str
    status:str
    platform:str
    stops:list[Stop]

@dataclass
class Board:
    station:str
    trains:list[Train]


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


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=80, debug=1)