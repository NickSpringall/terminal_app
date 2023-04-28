import xml.etree.ElementTree as ET
tree = ET.parse('product_database.xml')
root = tree.getroot()
from xml.dom import minidom 
import os
import pprint

from search_functions import prod_search, disp_full, disp_category, disp_keyword 
from item_display_functions import product_disp, sort_display_order
from cart_functions import add_to_cart, search_restart


sort_display_order(product_disp(prod_search()))

search_restart(add_to_cart())

