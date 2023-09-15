
import requests

api_prefix = "http://makeup-api.herokuapp.com/api/v1/products.json"

params = {
    "rating_greater_than": 3,
}

response = requests.get(api_prefix, params=params)

response.status_code
data = response.json()

#dictionaries for categorization
products_by_type = {}
product_counts = {}

for product in data:
    product_type = product['product_type']
    if product_type not in products_by_type:
        products_by_type[product_type] = []
        product_counts[product_type] = 1
    else:
        product_counts[product_type] += 1
    products_by_type[product_type].append(product)

for product_type, products in products_by_type.items():
    print(f"Product Type: {product_type} ({product_counts[product_type]} products)")
    for product in products:
        print(f"Product Name: {product['name']}")

    print()  #allows for spacing in between different categories


#code for ratings that are less than 3
api_prefix2 = "http://makeup-api.herokuapp.com/api/v1/products.json"

params = {
    "rating_less_than": 3,
}

response = requests.get(api_prefix2, params=params)


response.status_code
data = response.json()

products_by_type = {}
product_counts = {}

for product in data:
    product_type = product['product_type']
    if product_type not in products_by_type:
        products_by_type[product_type] = []
        product_counts[product_type] = 1
    else:
        product_counts[product_type] += 1
    products_by_type[product_type].append(product)

    
for product_type, products in products_by_type.items():
    print(f"Product Type: {product_type} ({product_counts[product_type]} products)")
    for product in products:
        print(f"Product Name: {product['name']}")
    print()  #adding a space in between categories for clearer visual
    

   