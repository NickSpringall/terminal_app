import xml.etree.ElementTree as ET

def write_prod_to_cart_function(file_name, dict_name):
    tree_cart = ET.parse(file_name)
    root_cart = tree_cart.getroot()

    items = root_cart.find("items")
    cart_item = ET.SubElement(items, "item")
    for i, (k, v) in enumerate(dict_name.items()):
        prod_text = str(v)
        key_val = str(k)
        product = ET.SubElement (cart_item, key_val)
        product.text = prod_text
        ET.indent (tree_cart, space = '\t')
        
    root_cart.append(product)
    weight = root_cart.find("weight")
    root_cart.remove(weight)
    tree_cart.write(file_name)