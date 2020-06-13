import sqlite3

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        print(e)
    return conn

def inserting(name,clas):
    sql_statement = "INSERT INTO student (Name,Class) VALUES (?,?);"
    new_db = sqlite3.connect("shitty 1NF db.db")
    cur = new_db.cursor()
    cur.execute(sql_statement,(name,clas))
    new_db.commit()
    #print(f"inserting {main_data[1]}")
    new_db.close()


file_handle = open("name.txt")
for i in file_handle:
    inserting(i.strip(),"19SH07")
    print(i.strip(),"19SH07")
file_handle.close()