import config
from order_summary_functions import order_summary
from checkout_functions import sub_total
import xml.etree.ElementTree as ET


def listen_for_quit_view_checkout(input):
    input = input.lower()

    if input == "quit":
        print("Thankyou for visiting the shop, we hope to see you again soon.")
        exit()
    if input == "view cart":
        tree_cart = ET.parse(config.z)
        root_cart = tree_cart.getroot()
        for item in root_cart.findall ("./items/item"):

            # prod_name = item[0].text
            name = item[2].text
            
            # prod_price = item[4].text
            price = item[4].text

            quantity = item[0].text

            print("Product --" + str(name) + "price/unit -- $" + str(price) + "quantity --" + str(quantity) + "sub total $" + str(float(price) * int(quantity)))
        return True

    if input == "checkout":
        pass

    else:
        return None
