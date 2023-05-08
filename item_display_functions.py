import pprint 
from operator import itemgetter
import xml.etree.ElementTree as ET

from tools import remove_letters_to_float

tree = ET.parse('product_database.xml')
list_root = tree.getroot()


# appends searched items to be displayed from product database to a list of dictionaries
def product_disp(list):
    ls_items_dict = []
    for x in list:
        for item in list_root:
            if item.attrib == x:
                item_dict = {"-":"-----------------------------------------------------------------"}

                for sub in item:
                    if sub.tag == "keywords":
                        continue
                    else:
                        item_dict[sub.tag] = sub.text
                        continue
    
                ls_items_dict.append(item_dict)
    return ls_items_dict


# Removes letters and returns an ordered list based on the chosen key in a list
def int_order(list, category_key, order):
    for x in list:
        cat = remove_letters_to_float (x[category_key])
        x[category_key] = cat
    return sorted(list, key=lambda d: d[category_key], reverse=order)
   

def add_back_dollar_sign(list):
    for x in list:
        x['price'] = "$" + str(x['price'])


# Prints sorted list of items returned in the search
def sort_display_order(list):
    while True:
        try:
            order_choice = int(input("How would you like the results to be sorted? \n type the number associated with your choice \n 1 - Highest price first \n 2 - lowest price first \n 3 - alphabetical \n 4 - weight \n 5 - Category: \n"))
            break
        except ValueError:
            print("-----Please only input a number between 1 and 5 as per the options below:-----")

    if order_choice == 1:
        ordered_list = (int_order(list, 'price', True))
        add_back_dollar_sign(ordered_list)
        pprint.pprint (ordered_list)

    elif order_choice == 2:
        ordered_list = (int_order(list, 'price', False))
        add_back_dollar_sign(ordered_list)
        pprint.pprint (ordered_list)
        
    elif order_choice == 3:
        for x in list:
            name = x['name']
            name_lower = name.lower()
            x['name'] = name_lower
        ordered_list = (sorted(list, key=itemgetter('name'), reverse=False))
        add_back_dollar_sign(ordered_list)
        pprint.pprint (ordered_list)

    elif order_choice == 4:
        ordered_list = (int_order (list, 'weight', False))
        for x in ordered_list:
            x['weight'] = str(x['weight']) + "kg"
            pprint.pprint (ordered_list)
     
    else:
        ordered_list = (sorted(list, key=lambda d: d['category'], reverse=False))
        add_back_dollar_sign(ordered_list)
        pprint.pprint (ordered_list)