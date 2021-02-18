import mysql.connector
mydb = mysql.connector.connect(
host = "localhost",
user = "root",
password = "password",
database = "app",
auth_plugin='mysql_native_password'
)
mycursor = mydb.cursor(dictionary=True)

# choice = int(input("Select a courier to delete starting from 1: "))

# sql = f"DELETE FROM test WHERE test_id={choice}"

# mycursor.execute(sql)

# mydb.commit()

# print(mycursor.rowcount, "record(s) deleted")

# sql = 'UPDATE test SET test_name = %s, test_phone = %s WHERE test_id = %s'

# courier_id = int(input('\nChoose a courier to update starting from 1 or type  to cancel: '))
# new_courier_name = input("\nWhat's the name of the new courier: ").strip().capitalize()
# new_courier_phone = (input("\nWhat's phone number of the new courier: "))
# courier_values = (new_courier_name, new_courier_phone, courier_id)
# mycursor.execute(sql, courier_values)
# mydb.commit()
new_courier = str(input("Please add couriers name : \n"))
courier_phone = int(input("Please add couriers phone number: \n"))
sql = "INSERT INTO test (test_name, test_phone) VALUES (%s, %s)"
val = (new_courier, courier_phone)
mycursor.execute(sql, val)
mydb.commit()
print(f"{new_courier} was succesfully added.")