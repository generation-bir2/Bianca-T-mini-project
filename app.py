import sys
import os
import csv
import mysql.connector
import json
from orders import *


def print_orders():
    shape = " "
    sql = 'SELECT * from orders'
    orders = read_db(sql)    
    for i in range(len(orders)):
            shape = '\n'
            for key, value in orders[i].items():
                    shape += f'{key}: {value}\n'
            print(shape)

def show_couriers_menu():
    print('''
            0: Return to main menu
            1: Couriers
            2: Create a new courier
            3: Update a courier
            4: Delete a courier \n''')
def clear():
    os.system( 'clear' )

def exit_app():
    sys.exit(0)

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

def print_products():
    shape = " "
    sql = 'SELECT * from products'
    products = read_db(sql)
    for item in products:
        item_id = item["product_id"]
        Name = item["product_name"]
        Price = item["product_price"]
        shape = f' ID:{item_id:} - {Name} : £{Price}'
        print(shape)
    return products

def print_couriers():
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

#orders shape
def print_orders():
    shape = " "
    sql = 'SELECT * from orders'
    orders = read_db(sql)    
    for i in range(len(orders)):
        shape = '\n'
        for key, value in orders[i].items():
                shape += f'{key}: {value}\n'
        print(shape)


def main_menu():
    print('''
                0 Exit App and Save
                1 Show products menu
                2 Show couriers menu 
                3 Show order menu
                ''')
    
def show_products_menu():   
    print('''
                0: Return to main menu
                1: Products
                2: Create a new product
                3: Update a product
                4: Delete a product \n''')
    

    
def show_orders_menu():
    print('''
                0: Return to main menu
                1: Orders
                2: Create a new order
                3: Update order status
                4: Update order
                5: Delete order \n''')

def products_menu():
    while True:
        show_products_menu()
        user_option = int(input("\n Select an option: "))
        if user_option == 0:
            break
        elif user_option == 1:
            print_products()
            
            #allows the user to go back and lets him know if the input is wrong
            while True:
                        user_option = int(input(''' \nSelect an option: \n
                0: Main menu 
                1: Products menu '''))
                        if user_option == 0:
                            return 
                        if user_option == 1:
                            break
                        else:
                                print("\n Incorect input, you need to choose 0 or 1!\n")
                                
        elif user_option == 2:
            print_products()
            new_product = str(input("Please add new product :\n "))
            new_price = float(input("Please add the price: \n "))
            sql = "INSERT INTO products (product_name, product_price) VALUES (%s, %s)"
            val = (new_product, new_price)
            save_db(sql, val)
            print("Product was succesfully added.")
        
        elif user_option == 3:
            print_products()
            product_id = int(input('\n Choose the product that you want to update or press 0 to cancel: '))
            if product_id == 0:
                return
            
            new_product = input("\n Please enter the new product: ")
            sql = "UPDATE products SET product_name = %s WHERE product_id = %s"
            if new_product !="":
                val = (new_product, product_id)
                save_db(sql,val)
                
            new_price = float(input("\n Please enter product's price: "))
            sql = "UPDATE products SET product_price = %s WHERE product_id = %s"
            if new_price !="":
                val = (new_price, product_id)
                save_db(sql,val)
                
            print(f"\nProduct nr {product_id} was succesfully updated.")
        
        elif user_option == 4:
            print_products()
            print('\n')
            product_delete = int(input("Choose the product that you want to delete or press 0 to cancel: \n"))
            if product_delete == 0:
                return
            sql = f"DELETE FROM products WHERE product_id={product_delete}"
            delete_db(sql)
            print( f"\n Product nr {product_delete} was successfully deleted.")
            

def couriers_menu():
    while True:
        show_couriers_menu()
        user_option = int(input("Select an option: "))
        print("\n")
        if user_option == 0:
            return
        elif user_option == 1:
            print_couriers()
            
        elif user_option == 2:
            new_courier = str(input("\n Please add courier's name : "))
            courier_phone = int(input("\n Please add courier's phone number: "))
            sql = "INSERT INTO couriers (couriers_name, couriers_phone) VALUES (%s, %s)"
            val = (new_courier, courier_phone)
            save_db(sql, val)
            print(f"\n {new_courier} was succesfully added.")
                    
        elif user_option == 3:
            print_couriers()
            
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
            print_couriers()
            deleted_couriers = int(input("\nChoose the courier that you want to delete or press 0 to cancel: "))
            if deleted_couriers == 0:
                return
            sql = f"DELETE FROM couriers WHERE couriers_id={deleted_couriers}"
            delete_db(sql)
            print( f"\nCourier nr {deleted_couriers} was successfully deleted.")
            



#main menu 
while True:
    clear()
    print( '''
        Welcome to caffe                         
    \n''')
    main_menu()
    user_option = int(input(" Select an option: "))
    if user_option == 0:
        exit_app()  
    elif user_option == 1:
        products_menu()
    elif user_option == 2:
        couriers_menu()
    elif user_option == 3:
        orders_menu()
        