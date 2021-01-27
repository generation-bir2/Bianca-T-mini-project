import sys
import os

print('Welcome to cafe royal!'+ '\n')
def clear():
  os.system( 'clear' )

def exit_app():
  sys.exit(0)
  
#this method is responsible for exiting the app or return the products menu
def main_menu():
  print('''
        0 Exit App
        1 Show products menu
        ''')
  


products = ["Coke","Coke Zero","Latte","Flat Whitte","Expresso","Panini","Croissant"]
print('\n')

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
  choice = int(input("Choose the product that you want to update starting from 0: "))
  new_product1 = input("Enter the new product: ")
  products[choice] = new_product1

def delete_product():
  delete_products = int(input("Select a product to delete starting from 0: "))
  products.pop(delete_products)

def show_products():
  print(products)
  print(' ')
  
#expect an input from the user
def products_menu():
  while True:
    show_products_menu()
    user_option = int(input("\n Select an option: "))
    if user_option == 0:
      break
    elif user_option == 1:
      show_products()
    elif user_option == 2:
      show_products()
      create_new_product()
      show_products() 
    elif user_option == 3:
      show_products()
      update_product()
      show_products()
    elif user_option == 4:
      show_products()
      delete_product()
      show_products()

#Shows the main menu, requires input from user 0 exit app, 1 showing the second menu
while True:
      main_menu()
      user_option = int(input("Select an option: "))
      if user_option == 0:
        exit_app()  
      elif user_option == 1:
        products_menu()