from write_prod_to_cart_function import write_prod_to_cart
from postage_functions import total_shipping_weight
import xml.etree.ElementTree as ET


# test writes a dictionary to a test xml file with write_prod_to_cart function and copies back the results to another dictionary
# If original dict and read back dict are identical the test passes
# second test case checks result for different sized and formatted dictionary compared to what is used in the program
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


# Test reads weight and quantity information from an xml and calculates the total weight, returning an integer
# first test case tests against file of identical format to the cart, second test case tests with different/random tag values and other non-numerical values
def test_total_shipping_weight():
    weight = total_shipping_weight("weight_test_1.xml")
    weight_2 = total_shipping_weight("weight_test_2.xml")

    assert weight == 30
    assert weight_2 == 1220