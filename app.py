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

def save_products():
  with open("products.txt", "w") as file:
      for product in products:
            file.write(product + "\n")
    


#this method is responsible for exiting the app or return the products menu
def main_menu():
  print('''
        0 Exit App
        1 Show products menu
        ''')
  

#this method only shows the products menu 
def show_products_menu():   
  print('''
        0: Return to main menu
        1: Products
        2: Select a product
        3: Update a product
        4: Delete a product \n''')

def create_new_product():
  new_product = str(input("Please add new product : \n"))
  products.append(new_product)
  
def update_product():
  choice = int(input("Choose the product that you want to update starting from 1: or 0 to cancel"))
  if choice == 0:
    return
  new_product1 = input("Enter the new product: ")
  products[choice-1] = new_product1

def delete_product():
  delete_products = int(input("Select a product to delete starting from 1: or 0 to cancel"))
  if delete_products == 0:
    return
  products.remove(products[delete_products-1])


def couriers_menu():
  
#expect an input from the user
def products_menu():
  while True:
    show_products_menu()
    user_option = int(input("\n Select an option: "))
    if user_option == 0:
      break
    elif user_option == 1:
      print(products)
    elif user_option == 2:
      print(products)
      create_new_product()
      print(products)
    elif user_option == 3:
      print(products)
      update_product()
      print(products)
    elif user_option == 4:
      print(products)
      delete_product()
      print(products)


#Shows the main menu, requires input from user 0 exit app, 1 showing the second menu
products = read_products()

while True:
  
  print('Welcome to cafe royal!'+ '\n')
  main_menu()
  user_option = int(input("Select an option: "))
  if user_option == 0:
        save_products()
        exit_app()  
  elif user_option == 1:
    products_menu()
  elif user_option == 2:
    couriers_menu()