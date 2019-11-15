import os
import sys
import sqlite3
from tabulate import tabulate
from datetime import datetime
# from termcolor import colored
# from tabulate import tabulate
# from colored import fg, attr

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'database.sqlite3')

# import code; code.interact(local=dict(globals(), **locals()))
conn = sqlite3.connect(DEFAULT_PATH)
cur = conn.cursor()

def list_todo():
  sql ="""
    SELECT * FROM todos 
  """

  cur.execute(sql)
  results = cur.fetchall()
  print(tabulate(results, headers=['id','body','user_id','date','status'], tablefmt='orgtbl'))
  conn.commit()



def add():
  sql ="""
      INSERT INTO todos
        (body, user_id, due_date)
      VALUES (?,?,?)
  """
  print('What do you want to add?')
  body = input()
  due_date = datetime.now()
  cur.execute(sql,(body, 1, due_date))
  conn.commit()
  print('body: ' + body + ' user_id: ' + str(1) + ' date: ' + str(due_date))

def show_help_menu():
  print("Here is your help")
def mark():
  print('What the project id do you want to change?')
  id_project = int(input())
  print('complete or incomplete')
  complete = int(input())
  if complete == 1:
    sql ="""
      UPDATE todos
      SET status = "complete"
      WHERE id = ?
    """
  if complete == 2:
    sql ="""
      UPDATE todos
      SET status = "incomplete"
      WHERE id = ?
    """
  cur.execute(sql,(id_project,))
  conn.commit()

if __name__  == '__main__':
    try:
      while True:
        print("What are you want to do?")
        choice = input()
        if choice == 'add':
          add()
        elif choice == 'list':
          list_todo()
        elif choice == 'mark':
          mark()
        else: show_help_menu()
    except:
      show_help_menu()
  #   arg1 = sys.argv[1]
  #   if arg1 == '--help':
  #     show_help_menu()
  #   else:
  #     fire.Fire({
  #       'do': do,
  #       'add': add,
  #       'undo': undo,
  #       'delete': delete,
  #       'list': show_list,
  #     })

      except IndexError:
        show_help_menu()
  #   sys.exit(1)
  