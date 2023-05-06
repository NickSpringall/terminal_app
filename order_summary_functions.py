import xml.etree.ElementTree as ET
import config

from tools import update_product_list, remove_letters_to_float

def order_summary(sub, ship, file_name):
    tree_cart = ET.parse(file_name)
    root_cart = tree_cart.getroot()

    order_total = sub + ship
    
    print("Thankyou for your order, your order total is $" + str(order_total))

    print("your order summary is - ") 
    for item in root_cart.findall ("./items/item"):

        # prod_name = item[0].text
        name = item[2].text
        
        # prod_price = item[4].text
        price = item[4].text

        price = remove_letters_to_float(price)

        quantity = item[0].text

        print("Product --" + str(name) + "price/unit -- $" + str(price) + "quantity --" + str(quantity) + "sub total $" + str((price) * int(quantity)))

        update_product_list(name, quantity)