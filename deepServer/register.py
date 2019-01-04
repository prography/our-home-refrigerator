import os
import sqlite3
from dbManage import createDB

def register(user_dir, db_name, ip):
    path = os.path.join(user_dir, db_name)
    if not os.path.exists(path):
        createDB()

    with sqlite3.connect(path) as conn:
        curs = conn.cursor()
        curs.execute("SELECT * FROM userManage")
        num = len(curs.fetchall()) + 1
        conn.commit()
        curs.execute("insert into userManage values ('" + num + "', '" + ip + "')")

    return ip