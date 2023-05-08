from os import path
import os
import re
from pathlib import Path


import config
import xml.etree.ElementTree as ET


def remove_abandoned_user_cart():
    if file_check("user_cart.xml") is True:
        os.remove("user_cart.xml")


def word_check(str, keyword):
    keyword_list = str.split()
    if keyword in str:
        return True
    else:
        return False
    

def file_check(file_name):
    address = path.exists(file_name)
    return address


def get_address():
    cwd = Path().absolute()
    return cwd


def is_selection_on_database(selection):
    tree = ET.parse('product_database.xml')
    list_root = tree.getroot()  
    for prod in list_root:
        if prod.attrib in config.x:
            if prod[0].text.lower() == selection.lower():
                return True
            else:
                continue


def is_keyword_selection_on_database(keyword):
    tree = ET.parse('product_database.xml')
    list_root = tree.getroot()
    all_keywords = []
    for prod in list_root:
        word_list = prod[5].text.split()
        all_keywords.append (word_list)

    all_keywords_flat = [item for sublist in all_keywords for item in sublist]
    if keyword in all_keywords_flat:
         return True
    

def get_stock_level(item):
    tree = ET.parse('product_database.xml')
    list_root = tree.getroot()

    for prod in list_root:
            if prod[0].text.lower() == item.lower():
                 for sub in prod:
                    if sub.tag == "left_in_stock":
                         stock = sub.text
    return stock


def update_product_list(product, quantity):

    tree = ET.parse('product_database.xml')
    list_root = tree.getroot()

    for item in list_root:
        if item[0].text == product:
            original_quant = item[6].text
            item[6].text = str(int(original_quant) - int(quantity))
    tree.write("product_database.xml")


def remove_letters_to_float(string):
    return float(re.sub("[^0-9.]", "", string))