import os

import xml.etree.ElementTree as ET
tree = ET.parse('product_database.xml')
list_root = tree.getroot()

def word_check(str, keyword):
    keyword_list = str.split()
    if keyword in str:
        return True
    else:
        return False
    

def file_check():
    exists = os.path.isfile("/Users/nickspringall/Desktop/Coder lessons/terminal_app/user_cart.xml")
    return exists


def get_stock_level(item):
    
    for prod in list_root:
            if prod[0].text.lower() == item.lower():
                 for sub in prod:
                    if sub.tag == "left_in_stock":
                         stock = sub.text
    return stock

