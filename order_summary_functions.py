import xml.etree.ElementTree as ET
import config
import os

from tools import update_product_list, remove_letters_to_float, get_address
from exception_functions import response_on_list_check


# Prints cart information and prompt the user to either save the cart or proceed with purchase
def order_summary(sub, ship, file_name):
    tree_cart = ET.parse(file_name)
    root_cart = tree_cart.getroot()
    order_total = sub + ship
    
    print("Your order total is $" + str(order_total))
    print("Your order summary is - ") 

    for item in root_cart.findall ("./items/item"):
        name = item[2].text
        price = item[4].text
        price = remove_letters_to_float(price)
        quantity = item[0].text
        print("Product --" + str(name) + " ||  price/unit -- $" + str(price) + "||  quantity --" + str(quantity) + "||  sub total $" + str((price) * int(quantity)))

    list = ("proceed", "save")
    proceed = response_on_list_check(input("Would you like to proceed with order of save cart for later? \n Please type 'proceed' or 'save':  "), list)

# If user proceeds with order, database is updated to reflect the new remaining stock levels
    if proceed == "proceed":
        update_product_list(name, quantity)
        file_name = str(get_address()) + "/" + config.y
        new_file_name = str(get_address()) + "/" + str("CONFIRMED" + config.y)
        os.rename(file_name, new_file_name)
        print ("Thankyou for your order, have a nice day")
        return
    else:
        print("Thankyou for visiting our store, have a nice day")