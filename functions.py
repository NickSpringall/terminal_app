
import xml.etree.ElementTree as ET
tree = ET.parse('product_database.xml')
root = tree.getroot()

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

    prod_num_list = []

    for item in root:
        for x in item.findall('category'):
            if x.text == cat_choice:
                prod_num_list.append(item.attrib)
            else:
                continue
    print(prod_num_list)

                
            
            # print out all data for items which have 



def disp_keyword():
    pass

def disp_full():
    pass



def prod_search():
    search_term = input ("Would you like to search by Catergory, Keyword or full list? (Type Catergory, Keyword or Full): ")
    if search_term.lower() == "category":
        disp_category()
    if search_term.lower == "keyword":
        disp_keyword()
    if search_term.lower == "full":
        disp_full()