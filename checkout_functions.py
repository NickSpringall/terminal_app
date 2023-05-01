import os
import xml.etree.ElementTree as ET
from datetime import date





def checkout():
    customerdict = {}
    user_first_name = input("Please enter your first name")
    user_surname = input("please enter your surname")
    user_phone_no = input("please enter your phone number")
    order_date = date.today()
    
    # write something to check if it's off this format, if they are happy allow it to continue
    user_address = input("please type your street address with the following format (with commas) - \n number street name, suburb, state, postcode \n foir example - 110 Street St, West End, QLD, 4000")

    # Create dictionary with customer's information
    for i in ('user_first_name', 'user_surname', 'user_phone_no', 'user_address', 'order_date'):
        customerdict[i] = locals()[i]

    tree_cart = ET.parse("user_cart.xml")
    root_cart = tree_cart.getroot()

    # write customer info to file
    if bool(root_cart.findall("customer", namespaces = None)) == True:
        next
    else: 
        customer = ET.Element("customer")
        root_cart.insert(0, customer) 
        ET.indent (tree_cart, space = '\t')

    customer = root_cart.find("customer")
    for i, (k, v) in enumerate(customerdict.items()):
        contact_text = str(v)
        key_val = str(k)
        info = ET.SubElement (customer, key_val)
        info.text = contact_text
        ET.indent (tree_cart, space = '\t')
    tree_cart.write("user_cart.xml")

    file_name = "/Users/nickspringall/Desktop/Coder lessons/terminal_app/user_cart.xml"
    new_file_name = "/Users/nickspringall/Desktop/Coder lessons/terminal_app/" + (user_first_name.lower() + "_" + user_surname.lower()) + ".xml"
    
    os.rename(file_name, new_file_name)

    def shipping_calc():
        tree_cart = ET.parse("user_cart.xml")
        root_cart = tree_cart.getroot()

    weight = "x"
    print(tree_cart.SubElement.findall(weight))
          

    


checkout()



# update XML name to user's actual name_cart

# calculate shipping from info
    # ask if they want express or standard
        # figure out a state by state shipping rate per kg and make a function
        # calculate total
        # save to cart.xml

# print summary of order

    # customer numer and details

    # product names
    # product quantity
    # unit cost
    # total cost

    # goods total
    # shipping type and cost
    # grand total

# ask for confirmation of details and order


# modify left in stock numbers
# generate warehouse picking file with product numbers, customer details, shipping details (express of standard)
