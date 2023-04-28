import os

def word_check(str, keyword):
    keyword_list = str.split()
    if keyword in str:
        return True
    else:
        return False
    
    
def file_check():
    exists = os.path.isfile("/Users/nickspringall/Desktop/Coder lessons/terminal_app/user_cart.xml")
    return exists