from tools import file_check
from exception_functions import yes_no_check
import config
import xml.etree.ElementTree as ET



def returning_user_check():
    cart_check = yes_no_check(input("Do you already have an active cart? Please input yes or no: "))

    file_name = "user_cart.xml"
    config.z = file_name

    if cart_check == "yes":
        user_first_name = input("please type your first name: ")
        user_surname = input("please type your surname: ")
        
        if file_check(user_first_name + "_" + user_surname + ".xml") == True:
            file_name = user_first_name + "_" + user_surname + ".xml"
            print ("Welcome back " + user_first_name)
            config.z = file_name

# remove existing postage info from cart if returning customer
            tree_cart = ET.parse(config.z)
            root_cart = tree_cart.getroot()
            items = root_cart.find('items')
            for x in items:
                for y in x:
                    if y.text == "express postage" or y.text == "standard postage":
                        items.remove(x)
                        tree_cart.write(config.z)

            return file_name
        else:
            print ("I'm sorry, we don't seem to have an active cart for you, please continue to create a new one")
            return file_name
    else:
        return file_name