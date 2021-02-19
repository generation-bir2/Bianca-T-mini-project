import os
import json
from databaseconnection import*
from products import *
from couriers import *

def clear():
  os.system( 'clear' )

def exit_app():
    sys.exit(0)

def show_orders_menu():
  print('''
          0: Return to main menu
          1: Orders
          2: Create a new order
          3: Update order status
          4: Update order
          5: Delete order \n''')

def print_orders(read_db):
  shape = " "
  sql = 'SELECT * from orders'
  orders = read_db(sql)    
  for i in range(len(orders)):
    shape = '\n'
    for key, value in orders[i].items():
      shape += f'{key}: {value}\n'
    print(shape)

def orders_menu(read_db, save_db, delete_db):
	while True:
		show_orders_menu()
		user_option = int(input("Select an option: "))
		print("\n")
		if user_option == 0:
			return
		elif user_option == 1:
			print_orders(read_db)
		
		elif user_option == 2:
			cust_name = str(input("Customer Name: "))
			cust_address = input("\nCustomer Address: ")
			cust_phone = int(input ("\nCustomer Phone: "))
			order_status = 'preparing'
		
			list_items = []
			products = print_products(read_db)
			while True:
				product = int(input("\nSelect product's id or Press 0 to finish: "))
				if product == 0:
					break
					
				product_inlist = False
				for item in products:
					if item['product_id'] == product:
						product_inlist = True
						list_items.append(product)
				if product_inlist == False:
					print("\nWe do not have this product, choose a product that matches the product's ID \n")
					
			print(f"\nThis is your order's list {list_items}")
			order_items = json.dumps(list_items)
			
			couriers = print_couriers(read_db)
			while True:
				couriers_id = int(input("\nSelect a courier from the list or press 0 to finish: \n"))
				if couriers_id == 0:
					break  
				
				sql = "INSERT INTO orders (customer_name, customer_address,customer_phone,couriers_id, order_status, items) VALUES (%s, %s, %s, %s, %s, %s)"
				val = (cust_name, cust_address, cust_phone, couriers_id, order_status, order_items)
				save_db(sql, val)
        

		elif user_option == 3:
			print_orders(read_db)
			updated_status = int(input('\nChoose an order by ID that you want to update its status or press 0 to cancel: '))
		
			if updated_status == 0:
				return
		
			status_list = ['preparing','ready to collect','delivered']
			shape = '\n'
			for i, item in enumerate(status_list):
				shape+= f'{i+1} - {item} \n'
			print(shape)
		
			new_status = int(input("\nPlease enter the new order status: "))-1
			sql = f"UPDATE orders SET order_status = '{status_list[new_status]}' WHERE order_id = {updated_status}"
			delete_db(sql)
			print("\nOrder status has been successfully updated.")
		
		elif user_option == 4:
			print_orders(read_db)
			order_id = int(input("\n Select an order to update or press 0 to cancel: "))
			if order_id == 0:
				return
			updated_name = input("\n Please enter the new customer's name or press enter to skip: ")
			sql = "UPDATE orders SET customer_name = %s WHERE order_id = %s"
			if updated_name !="":
				val = (updated_name, order_id)
				save_db(sql,val)
				
			updated_address = input("\n Please enter the new customer's address or press enter to skip: ")
			sql = "UPDATE orders SET customer_address = %s WHERE order_id = %s"
			if updated_address !="":
				val = (updated_address, order_id)
				save_db(sql,val)
				
			updated_phone = input("\n Please enter the new customer's phone or press enter to skip: ")
			print("")
			sql = "UPDATE orders SET customer_phone = %s WHERE order_id = %s"
			if updated_phone !="":
				val = (updated_phone, order_id)
				save_db(sql,val)
			
				sql = 'UPDATE orders SET items = %s WHERE order_id = %s'
				list_items = []
				print("")
				products = print_products(read_db)
				while True:
					product = int(input("\n Select a product's ID or press 0 to finish: "))
					if product == 0:
						break
						
					product_inlist = False
					for item in products:
						if item['product_id'] == product:
							product_inlist = True
							list_items.append(product)
					if product_inlist == False:
						print("\n We do not have this product, choose a product that matches the product's ID. \n")
						
					print(f"\n That's your order's list {list_items}")
					print("")
					order_items = json.dumps(list_items)
					val = (order_items, order_id)
					save_db(sql,val)
					
				sql = 'UPDATE orders SET couriers_id = %s WHERE order_id = %s'
				couriers = print_couriers(read_db)
			
			while True:
				update_courier = input("\n Please enter the new courier's ID or press enter to skip: ")
				
				if update_courier != '':
					order_val = (update_courier, order_id)
					try:
						save_db(sql, order_val)
						break
					except:
						print("\n Wrong courier ID, please choose a courier that matches the ID of the list ")
				else:
					break
			
			print('\n The order has been updated succesfully.')
		

		elif user_option == 5:
			print_orders(read_db)
			deleted_order = int(input("\n Choose an order to delete by its ID or press 0 to cancel:\n "))

			if deleted_order == 0:
				return
			sql = f"DELETE FROM orders WHERE order_id={deleted_order}"
			delete_db(sql)
			print( f"Order nr {deleted_order} was successfully deleted.")