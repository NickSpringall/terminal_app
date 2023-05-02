
import re
import config

from write_prod_to_cart_function import write_prod_to_cart_function

import xml.etree.ElementTree as ET

def total_shipping_weight():
        
    tree_cart = ET.parse(config.y)
    root_cart = tree_cart.getroot()

    total_weight = 0
    for item in root_cart.findall ("./items/item"):
        print (item[2].text)

        weight = item[6].text
        prod_weight = weight
        prod_weight_int = int(re.sub("[^0-9]", "", prod_weight))
        print(prod_weight_int)

        quantity = item[0].text
        prod_quant = int(quantity)
        print(prod_quant)

        total_weight = total_weight + (prod_weight_int * prod_quant)
    
    return total_weight


def shipping(package_weight):
    ship_price = ""
    standard_ship_per_kg = 3
    express_ship_per_kg = 5
    express_ship = express_ship_per_kg * int(package_weight)
    standard_ship = standard_ship_per_kg * int(package_weight)

    print("shipping options \n Standard 7 day shipping is $" + str(standard_ship) + "\n Next day express shipping is $" + str(express_ship))
 
    ship_method = input("Which method would you like? please type express or standard: ")
    if ship_method == "express":
        ship_price = express_ship
    elif ship_method == "standard":
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

    write_prod_to_cart_function(config.y, postage)

# def order_summary():
    
#     for item in root_cart.findall ("./items/item"):
#         print (item[2].text)


#     print("Thank you for your order, your order total is ")
    


