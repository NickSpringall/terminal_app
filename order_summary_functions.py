import xml.etree.ElementTree as ET
import config

from tools import update_product_list

def order_summary(sub, ship):
    tree_cart = ET.parse(config.y)
    root_cart = tree_cart.getroot()

    order_total = sub + ship
    
    print("Thankyou for your order, your order total is $" + str(order_total))

    print("your order summary is - ") 
    for item in root_cart.findall ("./items/item"):

        # prod_name = item[0].text
        name = item[2].text
        
        # prod_price = item[4].text
        price = item[4].text

        quantity = item[0].text

        print("Product --" + str(name) + "price/unit -- $" + str(price) + "quantity --" + str(quantity) + "sub total $" + str(float(price) * int(quantity)))

        update_product_list(name, quantity)


