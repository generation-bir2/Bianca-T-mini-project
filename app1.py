import sys
import os


def clear():
  os.system( 'clear' )

def exit_app():
  sys.exit(0)

def read_products():
  products = []
  with open("products.txt", "r") as file:
      for product in file:
          products.append(product.strip())
  return products

#printing the list into a 1,2,3,4 shape
def print_list(items):
  shape = "| "
  for i, item in enumerate(items):
      shape+= f'{i+1} - {item} | '
  print('\n', shape)
  

def print_orders():
  orders = [{"customer_name": "Matt",
            "customer_address": "Parade 21, London",
            "customer_phone" : "0123456788",
            "courier": 3,
            "order_status" : "preparing"
    
  },
  {         "customer_name": "Thomas",
            "customer_address": "23 Coten Lane, Coventry",
            "customer_phone" : "0123456788",
            "courier": 2,
            "order_status" : "preparing"
  }]
  
  for order in orders:  
    order_index = orders.index(order)
    print(f'Order number is {order_index}')
    for key, value in order.items():
      print(f'{key} : {value}')
    print('\n')

def save_products():
  with open("products.txt", "w") as file:
      for product in products:
        file.write(product + "\n")

def read_couriers():
  couriers = []
  with open ("couriers.txt", "r") as file:
      for courier in file:
          couriers.append(courier.strip())
  return couriers

def save_couriers():
  with open("couriers.txt", "w") as file:
      for courier in couriers:
        file.write(courier + "\n")

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
  
def show_couriers_menu():
  print('''
        0: Return to main menu
        1: Couriers
        2: Create a new courier
        3: Update a courier
        4: Delete a courier \n''')
  
def show_orders_menu():
  print('''
        0: Return to main menu
        1: Orders
        2: Create a new order
        3: Update order status
        4: Update order
        5: Delete order \n''')
      
def create_new_product():
  new_product = str(input("Please add new product :\n "))
  print('\n')
  products.append(new_product)
  
def update_product():
  choice = int(input("Choose the product that you want to update starting from 1: \n"))
  if choice == 0:
    return
  new_product1 = input("Enter the new product: ")
  products[choice-1] = new_product1

def delete_product():
  delete_products = int(input("Select a product to delete starting from 1: \n"))
  print("\n")
  if delete_products == 0:
    return
  products.remove(products[delete_products-1])

def products_menu():
  while True:
    show_products_menu()
    user_option = int(input("\n Select an option: "))
    if user_option == 0:
      break
    elif user_option == 1:
      print('\n')
      print_list(products)
      print('\n')
      #allows the user to go back and lets him know if the input is wrong
      while True:
            user_option = int(input(''' Select an option:
        0: Main menu 
        1: Products menu '''))
            if user_option == 0:
              return 
            if user_option == 1:
              break
            else:
                print("\n Incorect input, you need to choose 0 or 1!\n")
                
    elif user_option == 2:
      print_list(products)
      print(' ')
      create_new_product()
      print_list(products)
    elif user_option == 3:
      print_list(products)
      print('\n')
      update_product()
      print_list(products)
    elif user_option == 4:
      print_list(products)
      print('\n')
      delete_product()
      print_list(products)

def couriers_menu():
  while True:
    show_couriers_menu()
    user_option = int(input("Select an option: "))
    print("\n")
    if user_option == 0:
          return
    elif user_option == 1:
          print_list(couriers)
    
    elif user_option == 2:
      print_list(couriers)
      print("\n")
      new_courier = str(input("Please add new courier : \n"))
      couriers.append(new_courier)
      print_list(couriers)
          
    elif user_option == 3:
      print_list(couriers)
      print("\n")
      choice = int(input('Choose the courier that you want to update or press 0 to cancel: '))
      if choice == 0:
        return
      new_courier1 = input("Enter the new courier:\n ")
      couriers[choice-1] = new_courier1
      print_list(couriers)

    elif user_option == 4:
      print_list(couriers)
      delete_couriers = int(input("\nChoose the courier that you want to delete or press 0 to cancel: "))
      print("\n")
      if delete_couriers == 0:
        return
      couriers.remove(couriers[delete_couriers-1])
      print_list(couriers)

def orders_menu():
    while True:
      show_orders_menu()
      user_option = int(input("Select an option: "))
      print("\n")
      if user_option == 0:
        return
      elif user_option == 1:
        print_orders()
      
      elif user_option == 2:
        d = {}
        name = input("Please enter your name: ")
        d["Name"] = name
        address = input("Please enter your address: ")
        d["Address"] = address
        phone_number = input("Please enter your phone number: ")
        d["Phone number"] = phone_number
        print(d)
        
      elif user_option == 3:
        
        print("\n")
        update_status = int(input('Update order status or press 0 to cancel: '))
        if update_status == 0:
          return
        new_status = input("Enter the new status:\n ")
        d.update(= 3, z = 0)
        print(d)   
        
      elif user_option == 4:
        update_order = int(input("\n Select an order to update or press 0 to cancel: "))
        print("\n")
        if update_order == 0:
          return
        # if update_order = 1
        # pass
      
        
      elif user_option == 5:
        delete_order = int(input("\n Press 1 tot delete your order or press 0 to cancel: "))
        if delete_order == 0:
          return
        if delete_order == 1:
          d ={}
          del d["Address"]
          print("\n Your order details after you deleted :\n")
          print(str(d))

products = read_products()
couriers = read_couriers()

#main menu 
while True:
  clear()
  print('\n ******************* Welcome to cafe Royal! *********************\n')
  main_menu()
  user_option = int(input(" Select an option: "))
  if user_option == 0:
        save_products()
        save_couriers()
        exit_app()  
  elif user_option == 1:
    products_menu()
  elif user_option == 2:
    couriers_menu()
  elif user_option == 3:
    orders_menu()
    
        
#for csv
def products_menu():
      while True:
    show_products_menu()
    user_option = int(input("\n Select an option: "))
    if user_option == 0:
      break
    elif user_option == 1:
      print('\n')
      print_list(products)
      print('\n')
      #allows the user to go back and lets him know if the input is wrong
      while True:
            user_option = int(input(''' Select an option:
        0: Main menu 
        1: Products menu '''))
            if user_option == 0:
              return 
            if user_option == 1:
              break
            else:
                print("\n Incorect input, you need to choose 0 or 1!\n")
                
    elif user_option == 2:
      new_product = (input("Please add new product :\n "))
      new_price = int(input("Please add the price: \n "))
      new_dict = {
        "Products": new_product,
        "Price" : new_price,    
      }
      products.append(new_dict)
    
    elif user_option == 3:
      print_list(products)
      print('\n')
      choice = int(input ("Choose the product that you want to update starting from 1: \n"))
      updated_product = input("Enter the new product name: \n")
      updated_price = float(input("Enter the price of the new product: \n"))
      
      updated_dict = { "Products": updated_product,
                      "Price" : updated_price,
                    }
      products[choice -1] = updated_dict
      
    
    elif user_option == 4:
      print_list(products)
      print('\n')
      product_delete = int(input("Choose the product that you want to delete starting from 1: \n"))
      products.pop(product_delete - 1)
      print_list(products)
#csv
#def read_couriers():
    #   couriers_list = []
#   with open ("couriers.csv", "r") as file:
#     csv_file = csv.DictReader(file)
#     for courier in file:
#         couriers_list.append(courier)
#     return couriers_list
  
# couriers = read_couriers()
# def save_couriers():
#   keys = ["Name","Phone"]
#   with open("couriers.csv", "w", newline = "\n") as csvfile:
#     writer = csv.DictWriter(csvfile, keys)
#     writer.writeheader()
#     writer.writerows(couriers)

#orders csv 
# def read_orders():
#       orders_list = []
#   with open("orders.csv","r") as file:
#     csv_file = csv.DictReader(file)
#     for order in csv_file:
#           orders_list.append(order)
#     return orders_list  

# #orders shape
# def print_orders(items):
#   for i in range (len(orders)):
#       shape_d = f'Order: {i}\n'
#   for key, value in orders[i].items():
#       shape_d += f'{key}: {value}\n'
#   print(shape_d)
# for i, item in enumerate(items):
  #     couriers_name = item["couriers_name"]
  #     couriers_phone = item["couriers_phone"]
  #     shape+= f'{i+1} - {couriers_name} : {couriers_phone}  | '
  # print('\n', shape)
  

  # products =[]
        # product_index = int (input ("Select a product: \n"))
        # selected_product = products[product_index]
        # print_couriers()