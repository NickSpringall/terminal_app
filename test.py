from xml.dom import minidom 
import os

def add_to_cart():
    selection = input("Please type the name of the product you would like to order: ")
    quantity = int(input("how many would you like to order? "))

    file_check = os.path.isfile("/Users/nickspringall/Desktop/Coder lessons/terminal_app/current_order.xml")
    if file_check is False:
        root = minidom.Document()
        xml = root.createElement('user_cart')
        root.appendChild(xml)

        xml_str = root.toprettyxml(indent ="\t")
        save_path_file = "user_cart.xml"

        with open(save_path_file, "w") as f:
            f.write(xml_str)
    else:
        print("it's here")


