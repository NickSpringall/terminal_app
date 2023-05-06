import pprint 
from tools import remove_letters_to_float

import xml.etree.ElementTree as ET
tree = ET.parse('product_database.xml')
list_root = tree.getroot()
from operator import itemgetter

def product_disp(list):

    prods = [{
    }]

# x is list of item numbers
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

def int_order(list, category_key, order):
    for x in list:
        cat = remove_letters_to_float (x[category_key])
        x[category_key] = cat
    return sorted(list, key=lambda d: d[category_key], reverse=order)
   
def add_back_dollar_sign(list):
    for x in list:
        x['price'] = "$" + str(x['price'])


def sort_display_order(list):
    order_choice = int(input("how would you like the results to be sorted? \n type the number associated with your choice \n 1 - Highest price first \n 2 - lowest price first \n 3 - alphabetical \n 4 - weight \n 5 - Category \n"))
    if order_choice == 1:
        ordered_list = (int_order(list, 'price', True))
        add_back_dollar_sign(ordered_list)
        pprint.pprint (ordered_list)

    elif order_choice == 2:
        pprint.pprint(int_order(list, 'price', False))
        
    elif order_choice == 3:
        for x in list:
            name = x['name']
            name_lower = name.lower()
            x['name'] = name_lower
        pprint.pprint(sorted(list, key=itemgetter('name'), reverse=False))

    elif order_choice == 4:
        ordered_list = (int_order (list, 'weight', False))
        for x in ordered_list:
            x['weight'] = str(x['weight']) + "kg"
            pprint.pprint (ordered_list)
     
    else:
        pprint.pprint(sorted(list, key=lambda d: d['category'], reverse=False))

    