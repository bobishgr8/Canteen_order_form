import sqlite3
from rich.progress import track
from rich import print

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        print(e)
    return conn

new_db = sqlite3.connect("shitty 1NF db.db")

file_handle = open("process_alpha.txt")
main_data = []
for line in file_handle:
    main_data.append(line.strip().split(","))
file_handle.close()

def inserting(line_data):
    sql_statement = "INSERT INTO foods (stall_name, food_item, Price, day_avail) VALUES (?,?,?,?);"
    new_db = sqlite3.connect("shitty 1NF db.db")
    cur = new_db.cursor()
    cur.execute(sql_statement,(line_data[0],line_data[1],line_data[2],line_data[3]))
    new_db.commit()
    #print(f"inserting {main_data[1]}")
    new_db.close()
    
#sql_statement = "INSERT INTO foods (stall_name, food_item, Price, day_avail) VALUES (?,?,?,?);"
for line_data in main_data:
    inserting(line_data)
    print(f"Inserting {line_data[1]} into foods")
