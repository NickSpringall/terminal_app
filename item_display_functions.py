import pprint 


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


def sort_display_order(list):
    order_choice = int(input("how would you like the results to be sorted? \n type the number associated with your choice \n 1 - Highest price first \n 2 - lowest price first \n 3 - alphabetical \n 4 - weight \n 5 - Category \n"))
    if order_choice == 1:
        for x in list:
            price = x['price']
            price_float = float(price)
            x['price'] = price_float
        pprint.pprint(sorted(list, key=lambda d: d['price'], reverse=True))

    elif order_choice == 1:
        for x in list:
            price = x['price']
            price_float = float(price)
            x['price'] = price_float
        pprint.pprint(sorted(list, key=lambda d: d['price'], reverse=False))
        
    elif order_choice == 3:
        pprint.pprint(sorted(list, key=lambda d: d['name'], reverse=False)) 

    elif order_choice == 4:
        for x in list:
            weight = x['weight']
            
            weight_float = float(price)
            x['price'] = price_float
        pprint.pprint(sorted(list, key=lambda d: d['price'], reverse=False))

    



    if order_choice == 3:
        pprint.pprint(sorted(list, key=lambda d: d['name'], reverse=False))

        
def alphabetical():
    pprint.pprint(sorted(list, key=itemgetter('name'), reverse=True))
