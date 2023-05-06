from xml.dom import minidom 
import os
import pprint 
import config

import xml.etree.ElementTree as ET
tree = ET.parse('product_database.xml')
list_root = tree.getroot()

from tools import file_check, get_stock_level, is_selection_on_database
from item_display_functions import sort_display_order, product_disp
from search_functions import prod_search
from write_prod_to_cart_function import write_prod_to_cart_function
from exception_functions import yes_no_check

def add_to_cart():

    selection = input("Please type the name of a product from the list above that you would like to order: ")

    while is_selection_on_database(selection) == None:
        selection = input("Sorry, that is not on the list. \nPlease type the name of a product from the product list you would like to order: ")
    
    quantity = int(input("how many would you like to order? "))
    while quantity > int(get_stock_level(selection)):
        if int(get_stock_level(selection)) == 1:
            new_quant = input("Sorry, we only have" + str(get_stock_level(selection)) + selection + " in stock\n Please select another quantity or type 'search' to search for another product")
            if new_quant == "search":
                return
            else: 
                quantity = int(new_quant)
            # quantity = input("Sorry, we only have" + str(get_stock_level(selection)) + selection + " in stock\n Please select another quantity or type 'search' to search for another product")
        else: 
            new_quant = input("Sorry, we only have" + str(get_stock_level(selection)) + selection + "s in stock\n Please select another quantity or type 'search' to search for another product")
            if new_quant == "search":
                return
            else: 
                quantity = int(new_quant)

    # create shopping user_cart.xml file if it doesn't exist
    if file_check(config.z) is False:
        root = minidom.Document()
        xml = root.createElement(config.z)
        root.appendChild(xml)

        xml_str = root.toprettyxml(indent ="\t")
        save_path_file = "user_cart.xml"

        with open(save_path_file, "w") as f:
            f.write(xml_str)
        
    selection_to_cart = {
        "quantity": quantity,
        "prod_code": "",
        "name": "",
        "category": "",
        "price": "",
        "stock": "",
        "weight": ""
        }
    
# adding product details to dictionary from product_database.xml
    for item in list_root:
            if item[0].text.lower() == selection.lower():
                for sub in item:
                        if sub.tag == "name":
                            selection_to_cart["name"] = sub.text
                            selection_to_cart["prod_code"] = item.attrib
                        elif sub.tag == "category":
                            selection_to_cart["category"] = sub.text
                        elif sub.tag == "price":
                            selection_to_cart["price"] = sub.text
                        elif sub.tag == "left_in_stock":
                            selection_to_cart["stock"] = sub.text
                        elif sub.tag == "weight":
                            selection_to_cart["weight"] = sub.text

    
    # parse user cart
    tree_cart = ET.parse(config.z)
    root_cart = tree_cart.getroot()

    # check if the items sub tag exists in user_cart.xml and create one if not
    if bool(root_cart.findall("items", namespaces = None)) == True:
        next
    else:
        item = ET.Element("items")
        root_cart.append(item) 
        ET.indent (tree_cart, space = '\t')

# check if item already exists in cart and if sufficient stock is available
    items = root_cart.find("items")
    for x in items:
        if (bool(x[2].text.lower() == selection.lower())) is True:
            already_in_cart = int(x[0].text)
            current_stock = int(get_stock_level(selection))
            requested_stock = (already_in_cart + quantity)

            if current_stock <= requested_stock:
                print ("You already have " + str(already_in_cart) + " units of " + str(selection) + " in your cart and there are only " + str(current_stock) + " in stock")
                max_extra_units = current_stock - already_in_cart
                decision = input ("would you still like to purchase extra " + selection + " ?\n Type yes to update your quantity or No to return to search")
                if decision == "yes":
                    extra_units = int(input("how many extra units would you like to purchase? (up to " + str(max_extra_units) + ")"))
                    final_cart_units = (extra_units + already_in_cart)
                    selection_to_cart ["quantity"] = final_cart_units
                    for x in items:
                        for y in x:
                            if y.text == (selection):
                                items.remove(x)
                else:
                    selection_to_cart ["quantity"] = 0

            else:
                for x in items:
                    for y in x:
                        if y.text.lower() == (selection.lower()):
                            items.remove(x)
                            selection_to_cart["quantity"] = requested_stock

    items = root_cart.find("items")
    cart_item = ET.SubElement(items, "item")
    for i, (k, v) in enumerate(selection_to_cart.items()):
        prod_text = str(v)
        key_val = str(k)
        product = ET.SubElement (cart_item, key_val)
        product.text = prod_text
        ET.indent (tree_cart, space = '\t')
        
    root_cart.append(product)
    weight = root_cart.find("weight")
    root_cart.remove(weight)
    tree_cart.write(config.z)


def search_restart():

    next_step = yes_no_check(input("would you like to add another product?: "))
    
    if next_step == "yes":
        search_restart_point = input("would you like to view the previous list or see search options again? type 'previous list' or 'options' ")
        if search_restart_point == "options":
            return "restart", []
        if search_restart_point == "previous list":
            return "restart", config.x
    elif next_step =="no":
         print("go to checkout-----")
         return None, None