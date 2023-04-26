import xml.etree.ElementTree as ET
tree = ET.parse('product_database.xml')
root = tree.getroot()

from functions import prod_search, disp_category, disp_keyword


# for child in root:
#     print(child.tag, child.attrib)


# how to print out children and text
# for x in root:
#     for child in x:
#         print(child.text)


# for x in root:
#     for y in x.findall('description'):
#             if "chair" in y.text:
#                  print (y.text)




prod_search()