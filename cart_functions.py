from search_functions import prod_search, disp_category, disp_keyword

from xml.dom import minidom 
import os

import xml.etree.ElementTree as ET
tree = ET.parse('product_database.xml')
list_root = tree.getroot()


def selection(list):
    # print out item attributes if on the search list
    prods = {}

    for x in list:
        for item in list_root:
            if item.attrib == x:
                for sub in item:
                    print(sub.tag, sub.text)
                    prods.update({sub.tag: sub.text})
            else:
                continue
        else:
            continue
    return prods
    

def add_to_cart():
    selection = input("Please type the name of the product you would like to order: ")
    quantity = int(input("how many would you like to order? "))

    file_check = os.path.isfile("/Users/nickspringall/Desktop/Coder lessons/terminal_app/current_order.xml")
    if file_check is False:
        root = minidom.Document()
        xml = root.createElement('user_cart')
        root.appendChild(xml)

        customer = root.createElement('customer')
        xml.appendChild(customer)
        items = root.createElement('customer')
        xml.appendChild(items)
        

        xml_str = root.toprettyxml(indent ="\t")
        save_path_file = "user_cart.xml"

        with open(save_path_file, "w") as f:
            f.write(xml_str)
    
    name = ""
    category = ""
    price = ""
    weight = ""

    for item in list_root:
            if item[0].text.lower() == selection.lower():
                for sub in item:
                        if sub.tag == "name":
                            name = sub.text
                        elif sub.tag == "category":
                            category =  sub.text 
                        elif sub.tag == "price":
                            price = sub.text
                        elif sub.tag == "weight":
                            weight = sub.text



    
    # test = ""

    # for item in root:
    #     if item.text == selection:
    #         test = selection
    #         print(test)

