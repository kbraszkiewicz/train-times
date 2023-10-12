from flask import Flask

from flask import render_template
from dataclasses import dataclass
from flask import request
from flask import flash

from forms import Login

from flask import Flask, render_template, redirect, url_for
# from flask_bootstrap import Bootstrap5

from flask_wtf.csrf import CSRFProtect
from flaskext.mysql import MySQL
import hashlib

from liveData import getDepartureBoard
from data import Stop, Train, Board





app = Flask(__name__, static_folder='static')
csrf = CSRFProtect(app)


# Bootstrap-Flask requires this line
# bootstrap = Bootstrap5(app)
# Flask-WTF requires this line


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
    getBoard("LDS")
    train1 = Train("Leeds","HRS","19:45","On Time","6a","[stops]")
    train2 = Train("Leeds","HRS","19:45","On Time","6a","[stops]")
    board = Board("LDS",[train1,train2])
    return render_template("template.html",board=board)

@app.route("/station/<code>")
def station(code):

    print(getBoard(code))
    print(code)

    train1 = Train("Leeds","HRS","19:45","On Time","6a","[stops]")
    train2 = Train("Leeds","HRS","19:45","On Time","6a","[stops]")
    #board = Board("LDS",[train1,train2])
    board = getBoard(code)
    return render_template("template.html",board=board,code=code)

@app.route("/station/live/<code>")
def stationLive(code):
    print(code)
    board = getDepartureBoard(code)
    return render_template("template.html",board=board)

@app.route("/login", methods=['POST', 'GET'])
@csrf.exempt
def login():
    if request.method == 'POST':
        # check they exist
        email = request.form.get('email')
        password = request.form.get('password')

        password_hash = hashlib.sha512((email + '-' + password).encode('utf-8')).hexdigest()


        print(f'email= {email},password={password_hash}')
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(f'''SELECT * from user WHERE (email="{email}" AND pass="{password_hash}");''')
        data = cursor.fetchone()
        print(data)
        if data != None:
            return redirect(url_for('hello'))
        else:
            return render_template('login.html')
    return render_template('login.html')

@app.route("/register", methods=['POST','GET'])
@csrf.exempt
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(f'''SELECT * FROM user where email="{email}"''')
        data = cursor.fetchall()

        # check if account already exists
        print(len(data))
        if len(data) > 0:
            
            return redirect(url_for('register'))
        
        
        # hash pass
        password = request.form.get('password')
        conf_password = request.form.get('password-2')
        print(password,conf_password)

        if password != conf_password:
            flash('Error - Passwords do not match')
            print('passes dont match')
            return redirect(url_for('register'))

        password_hash = hashlib.sha512((email + '-' + password).encode('utf-8')).hexdigest()
        print(f'email= {email},password={password_hash}')
        # add new user creds to db
        cursor.execute(f'''INSERT INTO user (email, pass) VALUES ("{email}", "{password_hash}") ''')
        conn.commit()

        return redirect(url_for('hello'))

    return render_template('register.html')


# Returning board
def getBoard(dep_board):
    board = Board(dep_board,[])

    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute(f'''SELECT * FROM trains WHERE departure_station="{dep_board}";''')
    data = cursor.fetchall()

    for item in data:
        train = Train(
            item[1],
            item[2],
            item[4],
            item[5],
            item[6],
            item[3],
        )
        board.trains.append(train)        
    
    return board


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=1, use_reloader=True)
