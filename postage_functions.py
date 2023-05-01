import xml.etree.ElementTree as ET
import re
import config

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
    standard_ship_per_kg = 3
    express_ship_per_kg = 5


    print ("shipping options \n Standard 7 day shipping is" + str(standard_ship_per_kg * int(package_weight)) + "\n Next day express shipping is" + (express_ship_per_kg * package_weight))
