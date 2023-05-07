from write_prod_to_cart_function import write_prod_to_cart
from tools import get_address
import xml.etree.ElementTree as ET


# test writes a dictionary to a test xml file with write_prod_to_cart function and copies back the results to another dictionary
# If original and read back dictionaries are identical the test passes

def test_write_prod_to_cart():
       
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

    selection_2_to_cart = {
        "key1": "1",
        "key2": "2",
        "key3": "3",
        "weight": "4"
    }

    write_prod_to_cart('test.xml', selection_to_cart)
    write_prod_to_cart('test.xml', selection_2_to_cart)

    tree = ET.parse('test.xml')
    list_root = tree.getroot()

    check_file_1 = {
    }

    check_file_2 = {

    }

    items = list_root.find ("items")
    for x in items:
        if x[0].tag == "quantity":
            for y in x:
                key = y.tag
                value = y.text
                check_file_1.update({key : value})
        else:
            continue
    
    items = list_root.find ("items")
    for x in items:
        if x[0].tag == "key1":
            for y in x:
                key = y.tag
                value = y.text
                check_file_2.update({key : value})
        else:
            continue

    assert selection_to_cart == check_file_1
    assert selection_2_to_cart == check_file_2

