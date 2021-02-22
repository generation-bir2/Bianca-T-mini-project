import os

def show_products_menu():   
  print('''
          0: Return to main menu
          1: Products
          2: Create a new product
          3: Update a product
          4: Delete a product \n''')
  
def print_products(read_db):
  sql = 'SELECT * from products'
  products = read_db(sql)
  for item in products:
    item_id = item["product_id"]
    Name = item["product_name"]
    Price = item["product_price"]
    shape = f' ID:{item_id:} - {Name} : £{Price}'
    print(shape)
  return products

def products_menu(read_db, action_db):
  while True:
    show_products_menu()
    user_option = int(input("\nSelect an option: "))
    
    if user_option == 0:
      break
    elif user_option == 1:
      print("")
      print_products(read_db)
      
      #allows the user to go back and lets him know if the input is wrong
      while True:
        try:
          user_option = int(input(''' \nSelect an option: \n
          0: Main menu 
          1: Products menu '''))
        except:
          print("\nIncorrect input, you need to type a number, not a string!")
        if user_option == 0:
          return 
        if user_option == 1:
          break
        else:
          print("n\Incorrect input, you need to choose 0 or 1")
      
          
    #create new product  
    elif user_option == 2:
      print("")
      print_products(read_db)
      new_product = str(input("\n Please add new product : "))
      new_price = float(input("\n Please add the price:  "))
      sql = "INSERT INTO products (product_name, product_price) VALUES (%s, %s)"
      val = (new_product, new_price)
      action_db(sql, val)
      print("\n Product was succesfully added.")
  
    #update product
    elif user_option == 3:
      print("")
      print_products(read_db)
      product_id = int(input('\nChoose the product that you want to update or press 0 to cancel: '))
      if product_id == 0:
          return
      
      new_product = input("\nPlease enter the new product or press enter to skip: ")
      if new_product !="":
        sql = "UPDATE products SET product_name = %s WHERE product_id = %s"
        val = (new_product, product_id)
        action_db(sql,val)
          
  
      new_price = input("\nPlease enter product's price: ")
      if new_price !="":
        sql = "UPDATE products SET product_price = %s WHERE product_id = %s"
        val = (new_price, product_id)
        action_db(sql,val)
      print(f"\nProduct nr {product_id} was successfully updated.")
        
    # delete product
    elif user_option == 4:
      print("")
      print_products(read_db)
      product_delete = int(input("\nChoose the product that you want to delete or press 0 to cancel: "))
      if product_delete == 0:
          return
      sql = f"DELETE FROM products WHERE product_id={product_delete}"
      action_db(sql)
      print( f"\nProduct nr {product_delete} was successfully deleted.")