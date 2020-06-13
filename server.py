from flask import Flask, request , render_template
import sqlite3
from datetime import datetime as date
app = Flask(__name__)

day_cycle = ["Monday","Tuesday","Wednesday","Thursday","Friday"]

@app.route("/")
def landing():
    return render_template("index.html")

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        print(e)
    return conn

all_foods = {}

@app.route("/form")
def form():
    day_cycle = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
    new_db = create_connection("shitty 1NF db.db")
    cur = new_db.cursor()
    today = date.today().strftime("%A")
    if today == "Saturday" or today == "Sunday":
        order_day = "Monday"
    else:
        order_day = day_cycle[day_cycle.index(date.today().strftime("%A"))+1]

    cur.execute(f'select * from foods where day_avail like \'%{order_day}%\'')
    rows = cur.fetchall()

    stalls = {}
    for enum,row in enumerate(rows):
        if not(row[0] in stalls):
            stalls[f"{row[0]}"] = {"options":{enum:f"{row[1]}"}}
        else:
            stalls[f"{row[0]}"]["options"][enum] = f"{row[1]}"
    return render_template("form.html",Date=order_day,stalls=stalls)




if __name__ == "__main__":
    app.run(debug=True)
