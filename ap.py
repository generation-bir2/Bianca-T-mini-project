def read_products():
    products = []
    with open("products.txt", "r") as file:
        for product in file:
            products.append(product.strip())
    return products


products = read_products()
print(products)