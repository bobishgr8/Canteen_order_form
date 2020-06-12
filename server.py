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

def dynamic_form():
    new_db = sqlite3.connect("shitty 1NF db.db")
    cur = new_db.cursor()
    cur.execute(f'select * from foods where day_avail like \'%{day_cycle[day_cycle.index(date.today().strftime("%A"))+1]}%\'')
    rows = cur.fetchall()
    stalls = {}
    for row in rows:
        print(row)


dynamic_form()



@app.route("/form")
def form():
    new_db = sqlite3.connect("shitty 1NF db.db")
    cur = new_db.cursor()
    cur.execute(f'select * from foods where day_avail like \'%{day_cycle[day_cycle.index(date.today().strftime("%A"))+1]}%\'')
    rows = cur.fetchall()
    stalls = {}
    for row in rows:
        if not(row[0] in stalls):
            #JSON object {stall_name:{foods:price....food:price}
            stalls[f"{row[0]}"] = {row[1]:row[2]}
        else:
            pass



    return render_template("form.html")



"""
if __name__ == "__main__":
    app.run(debug=True)
"""
