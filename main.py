import xml.etree.ElementTree as ET
tree = ET.parse('product_database.xml')
root = tree.getroot()
from xml.dom import minidom 
import os
import pprint

from search_functions import prod_search, disp_category, disp_keyword
from cart_functions import selection, add_to_cart
# from test import add_to_cart



category_list = selection(prod_search())

add_to_cart()


