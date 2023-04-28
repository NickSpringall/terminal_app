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
    
    selection_to_cart = {
        "quantity": quantity
    }

    for item in list_root:
            if item[0].text.lower() == selection.lower():
                for sub in item:
                        if sub.tag == "name":
                            selection_to_cart["name"] = sub.text
                        elif sub.tag == "category":
                            selection_to_cart["category"] = sub.text
                        elif sub.tag == "price":
                            selection_to_cart["price"] = sub.text
                        elif sub.tag == "weight":
                            selection_to_cart["weight"] = sub.text

    print (selection_to_cart)
    
    tree_cart = ET.parse("user_cart.xml")
    root_cart = tree_cart.getroot()
    print(ET.tostring(root_cart))

    new_product = ET.Element("name")
    new_product.text = "hello"
    root_cart.append(new_product)
    print(new_product, new_product.text)

    tree_cart.write("user_cart.xml")


    # tree_cart = ET.parse("user_cart.xml")
    # root_cart = tree_cart.getroot()

    # for item in root_cart.findall("customer"):
    #     new=ET.SubElement(item, "name")
    #     new.text = selection_to_cart["name"]

    # parent = ET.Element("user_cart")
    # child_1 = ET.SubElement (parent, "child_1")
    # cart_xml = ET.tostring(child_1)
    # with open("user_cart.xml", "wb") as f:
    #     f.write(cart_xml)


    # for key in selection_to_cart:
    #     user_cart = ET.SubElement (user_cart, key)



       
    # print (name)
    # print (category)
    # print (price)
    # print (weight)




    
    # test = ""

    # for item in root:
    #     if item.text == selection:
    #         test = selection
    #         print(test)

