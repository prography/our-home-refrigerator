import os
import sqlite3

def switch(id, detection_dir='detection' ,switch_dir='switch', db_name='switch.db'):
    path = os.path.join(detection_dir, switch_dir)
    path = os.path.join(path, db_name)

    if not os.path.exists(path):
        with sqlite3.connect(path) as conn:
            curs = conn.cursor()
            curs.execute('create table switch (id)')
            conn.commit()
            print("[*] create database for switch")

    with sqlite3.connect(path) as conn:
        curs = conn.cursor()
        curs.execute("SELECT * FROM userManage")
        conn.commit()
        curs.execute("insert into switch values ('" + id + "')")
        conn.commit()
