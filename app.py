import sys
import os
import 
import mysql.connector
from products import *
from couriers import *
from orders import *

def clear():
  os.system('clear')

def exit_app():
  sys.exit(0)

def main_menu():
  print('''
          0 Exit App and Save
          1 Show products menu
          2 Show couriers menu 
          3 Show order menu
          ''')

#main menu 
while True:
  clear()
  print( '''
    __| |____________________________________________| |__
  ( __   ____________________________________________   __ )
      | |                                            | |
      | |                                            | |
      | |                                            | |
      | |           Welcome to Cafe Royal            | |
      | |                                            | |
      | |                                            | |
    __| |____________________________________________| |__
  ( __   ____________________________________________   __ )
      | |                                            | |                        
      \n''')
  
  main_menu()
  user_option = int(input(" Select an option: "))
  if user_option == 0:
    exit_app()  
  elif user_option == 1:
    products_menu(read_db, save_db, delete_db)
  elif user_option == 2:
    couriers_menu(read_db, save_db, delete_db)
  elif user_option == 3:
    orders_menu(read_db, save_db, delete_db)
      