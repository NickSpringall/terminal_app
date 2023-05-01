import xml.etree.ElementTree as ET
tree = ET.parse('product_database.xml')
root = tree.getroot()
from xml.dom import minidom 
import os
import pprint

from search_functions import prod_search
from item_display_functions import product_disp, sort_display_order
from cart_functions import add_to_cart, search_restart
from checkout_functions import checkout


sort_display_order(product_disp(prod_search()))

search_restart(add_to_cart())

checkout()


# todo - right some kind of function where any input can have a "Quit", "View Cart", "Go to checkout" "product search" option
        # build check out functions
        # build some kind of business side functions, viewing, updateing product database 
        # error handling
        # testing


