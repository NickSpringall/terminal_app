import os
import xml.etree.ElementTree as ET
import re

from datetime import date

from postage_functions import total_shipping_weight
from tools import remove_letters_to_float, get_address
from exception_functions import yes_no_check
import config

def user_details_already_in_cart():
    tree_cart = ET.parse(config.z)
    root_cart = tree_cart.getroot()
    

    if bool(root_cart.findall("customer", namespaces = None)) == True:
        next
    else: 
        customer = ET.Element("customer")
        root_cart.insert(0, customer) 
        ET.indent (tree_cart, space = '\t')
        tree_cart.write(config.z)

    customer = root_cart.find("customer")
    if not customer:
        return False
    
    else:
        for x in customer:
            print (x.tag + "----" + x.text)
        current_details_correct = yes_no_check(input("Are these still your current details? please type 'yes' or 'no':  "))
        if  current_details_correct == "yes":
            return True
        else:
            root_cart.remove(customer)
            tree_cart.write(config.z)
            return False

def checkout():
    try:
        if user_details_already_in_cart() == False:
            customerdict = {}
            user_first_name = input("Please enter your first name:  ")
            user_surname = input("Please enter your surname:  ")
            user_phone_no = input("Please enter your phone number:  ")
            order_date = date.today()
            user_address = input("Please type your street address with the following format (with commas) - \n number street name, suburb, state , postcode \n for example - 110 Street St, West End, QLD, 4000:"  )
   

 # Create dictionary with customer's information
            for i in ('user_first_name', 'user_surname', 'user_phone_no', 'user_address', 'order_date'):
                customerdict[i] = locals()[i]
            
            # update new filename to config.y
            config.y = user_first_name.lower() + ("_") + user_surname.lower() + (".xml")
    
            tree_cart = ET.parse(config.z)
            root_cart = tree_cart.getroot()

    # write customer info to file
            if bool(root_cart.findall("customer", namespaces = None)) == True:
                next
            else: 
                customer = ET.Element("customer")
                root_cart.insert(0, customer) 
                ET.indent (tree_cart, space = '\t')
            customer = root_cart.find("customer")

            for i, (k, v) in enumerate(customerdict.items()):
                contact_text = str(v)
                key_val = str(k)
                info = ET.SubElement (customer, key_val)
                info.text = contact_text
                ET.indent (tree_cart, space = '\t')
            tree_cart.write(config.z)

            file_name = str(get_address()) + "/" + config.z
            print (file_name)
            new_file_name = str(get_address()) + "/" + config.y
            print (new_file_name)
            os.rename(file_name, new_file_name)

        else:
            config.y = config.z

    except FileNotFoundError:
        print ("You went to checkout with nothing in your cart! ----- Exiting the shop, see you again soon")
        exit()


def sub_total(file_name):
    tree_cart = ET.parse(file_name)
    root_cart = tree_cart.getroot()

    total_price = 0
    for item in root_cart.findall ("./items/item"):
        prod_price = item[4].text
        price = prod_price
        prod_price_float = remove_letters_to_float(price)

        quantity = item[0].text
        prod_quant = quantity
        total_price = total_price + (float(prod_price_float) * int(prod_quant))
    
    print("The subtotal of your order is $" + str(total_price))

    return total_price