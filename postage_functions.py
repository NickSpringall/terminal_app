import config

from write_prod_to_cart_function import write_prod_to_cart
from tools import remove_letters_to_float

import xml.etree.ElementTree as ET

# calculates weight of all items in cart
def total_shipping_weight(file_name):
        
    tree_cart = ET.parse(file_name)
    root_cart = tree_cart.getroot()

    total_weight = 0
    for item in root_cart.findall ("./items/item"):
        for x in item:
            if x.tag == "weight":
                weight = x.text
                prod_weight = weight
                prod_weight_int = remove_letters_to_float(prod_weight)
                
                for x in item:
                    if x.tag == "quantity":
                        quantity = x.text

                        prod_quant = int(quantity)

                        total_weight = total_weight + (prod_weight_int * prod_quant)
    print (total_weight)
    return total_weight

# Calculates standard and express shipping cost and prompts user to chose between them
def shipping(package_weight):
    ship_price = ""
    standard_ship_per_kg = 3
    express_ship_per_kg = 5
    express_ship = express_ship_per_kg * int(package_weight)
    standard_ship = standard_ship_per_kg * int(package_weight)

    print("Shipping options \n Standard 7 day shipping is $" + str(standard_ship) + "\n Next day express shipping is $" + str(express_ship))
    ship_method = ""
    while ship_method.lower() != "express" and ship_method != "standard":
        ship_method = input("Which method would you like? please type express or standard:  ")

    if ship_method.lower() == "express":
        ship_price = express_ship
    elif ship_method.lower() == "standard":
        ship_price = standard_ship

    postage = {
        "quantity": "1",
        "prod_code": "",
        "name": ship_method + " postage",
        "category": "",
        "price": ship_price,
        "stock": "",
        "weight": ""
    }

# Writes postage information to cart as another product
    write_prod_to_cart(config.y, postage)
    return ship_price