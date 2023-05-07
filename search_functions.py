import xml.etree.ElementTree as ET
tree = ET.parse('product_database.xml')
root = tree.getroot()

from tools import word_check, is_keyword_selection_on_database
from exception_functions import response_on_list_check
import config


def disp_category():
    prod_num_list = []
    cat_list = []
    for item in root:
        for x in item.findall('category'):
            if x.text not in cat_list:
                cat_list.append(x.text)
            else:
                continue

    print ("Please select from the following categories -")
    print (cat_list)
    cat_choice = response_on_list_check(input("Choice:  "), cat_list)

    for item in root:
        for x in item.findall('category'):
            if x.text == cat_choice:
                prod_num_list.append(item.attrib)
            else:
                continue
    return (prod_num_list)

def disp_keyword():
    prod_num_list = []
    user_keyword = input("Please type in a keyword to search:\n")
    while is_keyword_selection_on_database(user_keyword) is not True:
        user_keyword = input("Sorry, that keyword returned no results, please type in another keyword to search or 'search' to search another way:\n")
        if user_keyword == "search" or user_keyword == "Search":
            return ["search_again"]

    for item in root:
        for x in item.findall('keywords'):
            if word_check(x.text, user_keyword) is True:
                prod_num_list.append(item.attrib)
            continue
    return (prod_num_list) 


def disp_full():
    prod_num_list = []
    for item in root:
        prod_num_list.append(item.attrib)

    return (prod_num_list)


def prod_search(list):
    if list != []:
        return (list)
    
    prod_num_list = ["search_again"]
    while prod_num_list == ["search_again"]:
        cat_options = ("Category", "Keyword", "Full")
        search_term = response_on_list_check(input ("Would you like to search by Catergory, Keyword or Full list? (Type Category, Keyword or Full):  "), cat_options)

        if search_term == "category":
            prod_num_list = disp_category()
            config.x = prod_num_list

        if search_term == "keyword":
            prod_num_list = disp_keyword()
            config.x = prod_num_list
                
        if search_term == "full":
            prod_num_list = disp_full()
            config.x = prod_num_list

    print(prod_num_list)
    return (prod_num_list)