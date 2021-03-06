import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

#connects to the database
def db_connect():
  return mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='app',
    auth_plugin='mysql_native_password'
    )
  
#retrieves the content of the database
def read_db(sql):
  my_db = db_connect()
  mycursor = my_db.cursor(dictionary=True)
  mycursor.execute(sql)
  content = mycursor.fetchall()
  my_db.close()
  return content

#executes an action which can be insert/update/delete data from database
def action_db(sql, args=None):
  my_db = db_connect()
  mycursor = my_db.cursor(dictionary=True)
  mycursor.execute(sql,args)
  my_db.commit()
  mycursor.close()
  my_db.close()