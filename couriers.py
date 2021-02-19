import os
def clear():
  os.system('clear')

def show_couriers_menu():
    print('''
            0: Return to main menu
            1: Couriers
            2: Create a new courier
            3: Update a courier
            4: Delete a courier \n''')

def print_couriers(read_db):
    shape = " "
    sql = 'SELECT * from couriers'
    couriers = read_db(sql)
    for item in couriers:
      couriers_id = item["couriers_id"]
      couriers_name = item["couriers_name"]
      couriers_phone = item["couriers_phone"]
      shape = f'ID:{couriers_id} - {couriers_name} : {couriers_phone}'
      print(shape)
    return couriers

def couriers_menu(read_db, save_db, delete_db):
  while True:
    show_couriers_menu()
    user_option = int(input("Select an option: "))
    print("\n")
    if user_option == 0:
      return
    elif user_option == 1:
      print_couriers(read_db)
        
    elif user_option == 2:
      new_courier = str(input("\n Please add courier's name : "))
      courier_phone = int(input("\n Please add courier's phone number: "))
      sql = "INSERT INTO couriers (couriers_name, couriers_phone) VALUES (%s, %s)"
      val = (new_courier, courier_phone)
      save_db(sql, val)
      print(f"\n {new_courier} was succesfully added.")
                  
    elif user_option == 3:
      print_couriers(read_db)
      
      courier_id = int(input('\n Choose the courier that you want to update or press 0 to cancel: '))
      if courier_id == 0:
          return
      
      new_courier_name = input("\nWhat's the name of the new courier: ")
      sql = "UPDATE couriers SET couriers_name = %s WHERE couriers_id = %s"
      if new_courier_name !="":
        val = (new_courier_name, courier_id)
        save_db(sql,val)
          
      
      new_courier_phone = input("\nWhat's phone number of the new courier: ")
      sql = "UPDATE couriers SET couriers_phone = %s WHERE couriers_id = %s"
      if new_courier_phone !="":
        val = (new_courier_phone, courier_id)
        save_db(sql,val)
          
      print(f"\n Courier nr {courier_id} was succesfully updated.")
        
    elif user_option == 4:
      print_couriers(read_db)
      deleted_couriers = int(input("\nChoose the courier that you want to delete or press 0 to cancel: "))
      if deleted_couriers == 0:
        return
      sql = f"DELETE FROM couriers WHERE couriers_id={deleted_couriers}"
      delete_db(sql)
      print( f"\nCourier nr {deleted_couriers} was successfully deleted.")
