from flask import Flask
from flask import render_template
from dataclasses import dataclass
from flask import request

from forms import Login

from flask import Flask, render_template, redirect, url_for
# from flask_bootstrap import Bootstrap5

from flask_wtf.csrf import CSRFProtect






app = Flask(__name__, static_folder='static')
csrf = CSRFProtect(app)


# Bootstrap-Flask requires this line
# bootstrap = Bootstrap5(app)
# Flask-WTF requires this line


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


@app.route("/login", methods=['POST', 'GET'])
@csrf.exempt
def login():
    if request.method == 'POST':
            return redirect(url_for('hello'))
    return render_template('login.html')




# if __name__ == "__main__":

#     app.run(host="0.0.0.0")