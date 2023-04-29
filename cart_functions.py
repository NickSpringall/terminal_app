from xml.dom import minidom 
import os
import pprint 

import config
import search_functions

import xml.etree.ElementTree as ET
tree = ET.parse('product_database.xml')
list_root = tree.getroot()

from tools import file_check
from item_display_functions import sort_display_order, product_disp
from search_functions import prod_search

def add_to_cart():
    selection = input("Please type the name of the product you would like to order: ")

    # write function that lets user know how many left in stock and prevents them entering more
    quantity = int(input("how many would you like to order? "))

    # create shopping user_cart.xml file if it doesn't exist
    if file_check() is False:
        root = minidom.Document()
        xml = root.createElement('user_cart')
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
                        elif sub.tag == "weight":
                            selection_to_cart["weight"] = sub.text

    
    # parse user cart
    tree_cart = ET.parse("user_cart.xml")
    root_cart = tree_cart.getroot()

    # check if the items sub tag exists in user_cart.xml and create one if not
    if bool(root_cart.findall("items", namespaces = None)) == True:
        next
    else:
        item = ET.Element("items")
        root_cart.append(item) 
        ET.indent (tree_cart, space = '\t')

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
    tree_cart.write("user_cart.xml")
    
    next_step = input("would you like to add another product?: ")
    return next_step


def search_restart(response):
    
    if response == "yes":
        search_restart_point = input("would you like to view the previous list or see search options again? type 'previous list' or 'options' ")
        if search_restart_point == "previous list":
            sort_display_order(product_disp(config.x))
        if search_restart_point == "options":
            sort_display_order(product_disp(prod_search()))
    elif response =="no":
         print("go to checkout----")
         return