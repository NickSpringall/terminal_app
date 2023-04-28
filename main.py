import xml.etree.ElementTree as ET
tree = ET.parse('product_database.xml')
root = tree.getroot()
from xml.dom import minidom 
import os
import pprint

from search_functions import prod_search, disp_full, disp_category, disp_keyword 
from cart_functions import product_disp_order, add_to_cart


category_list = product_disp_order(prod_search())

add_to_cart()


