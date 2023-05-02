from tools import file_check

def returning_user_check():
    cart_check = input("Do you already have an active cart? Please input yes or no: ")
    if cart_check == "yes":
        user_first_name = input("please type your first name: ")
        user_surname = input("please type your surname: ")
        
        if file_check(user_first_name + "_" + user_surname + ".xml") == "exists":
            file_name = user_first_name + "_" + user_surname + ".xml"
            print ("Welcome back" + user_first_name)
            return file_name
        else:
            print ("I'm sorry, we don't seem to have an active cart for you, please continue to create a new one")
            file_name = "user_cart.xml"
            return file_name