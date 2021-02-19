def read_db(sql):
  my_db = mysql.connector.connect(
  host='localhost',
  user='root',
  password='password',
  database='app',
  auth_plugin='mysql_native_password'
  )
  mycursor = my_db.cursor(dictionary=True)
  mycursor.execute(sql)
  content = mycursor.fetchall()
  my_db.close()
  return content

def save_db(sql,args):
  my_db = mysql.connector.connect(
  host='localhost',
  user='root',
  password='password',
  database='app',
  auth_plugin='mysql_native_password'
  )
  mycursor = my_db.cursor(dictionary=True)
  mycursor.execute(sql,args)
  my_db.commit()
  mycursor.close()
  my_db.close()
  
def delete_db(sql):
  my_db = mysql.connector.connect(
  host='localhost',
  user='root',
  password='password',
  database='app',
  auth_plugin='mysql_native_password'
  )
  mycursor = my_db.cursor(dictionary=True)
  mycursor.execute(sql)
  my_db.commit()
  mycursor.close()
  my_db.close()