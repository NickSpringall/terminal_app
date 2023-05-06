def yes_no_check(response):

    if response.lower == "yes" or response.lower() == "no":
        return response
    
    while response.lower() != "yes" and response.lower() != "no":
        response = input("Incorrect input, please only type 'yes' or 'no': ")
    return response
