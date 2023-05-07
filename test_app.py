from write_prod_to_cart_function import write_prod_to_cart_function
from tools import get_address
import xml.etree.ElementTree as ET



def test_write_prod_to_cart_function():
       
    quantity = "10"
    selection_to_cart = {
        "quantity": quantity,
        "prod_code": "1234",
        "name": "test_product",
        "category": "test",
        "price": "$1,000,000",
        "stock": "20",
        "weight": "50kg"
        }

    write_prod_to_cart_function('test.xml', selection_to_cart)

    tree = ET.parse('test.xml')
    list_root = tree.getroot()

    check_file = {
    }

    items = list_root.find ("items")
    for x in items:
        for y in x:
            key = y.tag
            value = y.text
            check_file.update({key : value})

    assert selection_to_cart == check_file