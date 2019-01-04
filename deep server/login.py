import os
import sqlite3

def login(ip, user_dir, db_name):
    path = os.path.join(user_dir, db_name)
    try:
        with sqlite3.connect(path) as conn:
            curs = conn.cursor()
            curs.execute("SELECT * FROM userManage")
    except:

