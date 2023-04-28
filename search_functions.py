
import xml.etree.ElementTree as ET
tree = ET.parse('product_database.xml')
root = tree.getroot()

from tools import word_check


prod_num_list = []

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
    cat_choice = input ("Choice: ")

    for item in root:
        for x in item.findall('category'):
            if x.text == cat_choice:
                prod_num_list.append(item.attrib)
            else:
                continue
    return (prod_num_list)


def disp_keyword():
    user_keyword = input("please type in a keyword to search: ")
    for item in root:
        for x in item.findall('keywords'):
            if word_check(x.text, user_keyword) is True:
                print("true")
                prod_num_list.append(item.attrib)
            continue
    print (prod_num_list)
    return (prod_num_list) 


def disp_full():
    for item in root:
        prod_num_list.append(item.attrib)

    return (prod_num_list)


def prod_search():
    search_term = input ("Would you like to search by Catergory, Keyword or full list? (Type Catergory, Keyword or Full): ")
    
    if search_term.lower() == "category":
        prod_num_list = disp_category()
        
    if search_term.lower() == "keyword":
        prod_num_list = disp_keyword()

    if search_term.lower() == "full":
        prod_num_list = disp_full()
        print (prod_num_list)
    
    return (prod_num_list)