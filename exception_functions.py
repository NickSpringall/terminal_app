def yes_no_check(response):
    if response.lower == "yes" or response.lower() == "no":
        return response
    
    while response.lower() != "yes" and response.lower() != "no":
        response = input("Incorrect input, please only type 'yes' or 'no': ")
    return response


def no_numeric_chars_check(response):
    if any(char.isdigit() for char in response) is False:
        new_response = input("please only type letters, not numbers")
    return new_response

def no_letters_check(response):
    new_response = response
    while any(char.isnumeric() for char in new_response) is False:
        new_response = input("please only type numbers, not letters - ")
    return new_response

def response_on_list_check(response, list):
    on_list = False

    for x in list:
        if x.lower() == response.lower():
            return response

    while on_list is False:
        response = input("Choice not available, please type one of the options above: ")
        for x in list:
            if x.lower() == response.lower():
                on_list = True
    return response.lower()