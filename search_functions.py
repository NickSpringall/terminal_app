import xml.etree.ElementTree as ET
tree = ET.parse('product_database.xml')
root = tree.getroot()

from quit_view_checkout_function import listen_for_quit_view_checkout
from tools import word_check, is_keyword_selection_on_database
from exception_functions import no_numeric_chars_check, response_on_list_check

prod_num_list = []
import config
config.x = prod_num_list

def disp_category():
    cat_list = []
    for item in root:
        for x in item.findall('category'):
            if x.text not in cat_list:
                cat_list.append(x.text)
            else:
                continue

    print ("Please select from the following categories")
    print (cat_list)
    print (type(cat_list))

    cat_choice = response_on_list_check(input("Choice: "), cat_list)

    for item in root:
        for x in item.findall('category'):
            if x.text == cat_choice:
                prod_num_list.append(item.attrib)
            else:
                continue
    return (prod_num_list)


def disp_keyword():
    user_keyword = input("please type in a keyword to search:\n")
    while is_keyword_selection_on_database(user_keyword) is None:
        user_keyword = input("Sorry, that keyword returned no results, please type in another keyword to search:\n")

    for item in root:
        for x in item.findall('keywords'):
            if word_check(x.text, user_keyword) is True:
                prod_num_list.append(item.attrib)
            continue
    return (prod_num_list) 


def disp_full():
    for item in root:
        prod_num_list.append(item.attrib)

    return (prod_num_list)


def prod_search(prod_list):
    if prod_list != []:
        return prod_list
    else:
        cat_options = ("Category", "Keyword", "Full")
        search_term = response_on_list_check (input ("Would you like to search by Catergory, Keyword or Full list? (Type Category, Keyword or Full): "), cat_options)

        if search_term == "category":
            prod_num_list = disp_category()
                
        if search_term == "keyword":
            prod_num_list = disp_keyword()

        if search_term == "full":
            prod_num_list = disp_full()

        return (prod_num_list)