def read_products():
    products = []
    with open("products.txt", "r") as file:
        for product in file:
            products.append(product.strip())
    return products


products = read_products()
print(products)

while True:
            user_option = int(input("Select an option:0 to main menu \n 1 to couriers menu "))
            if user_option == 0:
                return 
            if user_option == 1:
                continue
            else:
                print("Incorect input, you need choose 0 or 1")
                
# d = {}

        # for i in range(n):
        #     keys = input() # here i have taken keys as strings
        #     values = int(input()) # here i have taken values as integers
        #     d[keys] = values
        # print(d)
        
        x = [str(x) for x in input("Enter your name, address and phone number: ").split(',')]
        print("Your details: ", x) 
        n = 3
        d = dict(x.split() for _ in range(n))
        print (d)
