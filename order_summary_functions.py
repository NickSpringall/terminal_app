import xml.etree.ElementTree as ET
import config
import os

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

        proceed = input("would you like to proceed with order of save cart for later? \n Please type 'proceed' or 'save'")
        if proceed == "proceed":
            update_product_list(name, quantity)
            file_name = "/Users/nickspringall/Desktop/Coder lessons/terminal_app/" + config.z
            new_file_name = "/Users/nickspringall/Desktop/Coder lessons/terminal_app/" + config.y + "CONFIRMED ORDER"
            os.rename(file_name, new_file_name)
            
