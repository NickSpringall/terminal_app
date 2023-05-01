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

import config
import search_functions

def is_selection_on_database(selection):
     for prod in list_root:
            if prod.attrib in config.x:
                if prod[0].text.lower() == selection.lower():
                    return True
                else:
                    continue


def is_keyword_selection_on_database(keyword):
    all_keywords = []
    for prod in list_root:
        word_list = prod[5].text.split()
        all_keywords.append (word_list)

    all_keywords_flat = [item for sublist in all_keywords for item in sublist]
    if keyword in all_keywords_flat:
         return True
    

def get_stock_level(item):
    
    for prod in list_root:
            if prod[0].text.lower() == item.lower():
                 for sub in prod:
                    if sub.tag == "left_in_stock":
                         stock = sub.text
    return stock


