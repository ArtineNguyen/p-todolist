import os
import sys
import sqlite3
from datetime import datetime
# import code
# from termcolor import colored
# from tabulate import tabulate
# from colored import fg, attr

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'database.sqlite3')

# code.interact(local=dict(globals(), **locals()))
conn = sqlite3.connect(DEFAULT_PATH)
cur = conn.cursor()

def setupTodos():
    sql = """
        CREATE TABLE IF NOT EXISTS todos(
            id INTEGER PRIMARY KEY,
            body TEXT NOT NULL,
            user_id INTEGER,    
            due_date TEXT NOT NULL,
            status TEXT DEFAULT "incomplete"
        )
    """
    cur.execute(sql)
    conn.commit()

def setupUser():
    sql = """
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY,
            email TEXT NOT NULL,
            birthday DATE NOT NULL
        )
    """
    cur.execute(sql)

    sql = """
        INSERT INTO users
            (email, birthday)
        VALUES (?,?)
    """

    cur.execute(sql,('artinenguyen@gmail.com', datetime.now()))
    conn.commit()


setupTodos()
setupUser()