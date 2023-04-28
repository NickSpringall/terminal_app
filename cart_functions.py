from xml.dom import minidom 
import os
import pprint 

import xml.etree.ElementTree as ET
tree = ET.parse('product_database.xml')
list_root = tree.getroot()

from tools import file_check


def add_to_cart():
    selection = input("Please type the name of the product you would like to order: ")
    quantity = int(input("how many would you like to order? "))

    
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

    
    # create items sub tag in user_cart then copy over product info
    tree_cart = ET.parse("user_cart.xml")
    root_cart = tree_cart.getroot()

    items = ET.Element("items")
    root_cart.append(items) 
    ET.indent (tree_cart, space = '\t')

    cart_item = ET.SubElement(items, "item")
    root_cart.append(cart_item)
    ET.indent (tree_cart, space = '\t')
    # tree_cart.write("user_cart.xml")

    for i, (k, v) in enumerate(selection_to_cart.items()):
        prod_text = str(v)
        key_val = str(k)

        product = ET.SubElement (cart_item, key_val)
        product.text = prod_text
        root_cart.append(product)
        ET.indent (tree_cart, space = '\t')
        tree_cart.write("user_cart.xml")

    next_step = input("would you like to add another product?: ")
    return next_step


def search_restart(response):
    
    if response == "yes":
        search_restart_point = input("would you like to view the previous list or see search options again? type 'previous list' or 'options' ")
        if search_restart_point == "previous list":
            pass
        if search_restart_point == "options":
            pass
    elif response =="no":
         print("go to checkout----")
         return


