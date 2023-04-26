import xml.etree.ElementTree as ET
tree = ET.parse('product_database.xml')
root = tree.getroot()

for child in root:
    print(child.tag)
