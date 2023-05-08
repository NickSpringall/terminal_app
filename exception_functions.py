def yes_no_check(response):
    if response.lower() == "yes" or response.lower() == "no":
        return response.lower()
    
    while response.lower() != "yes" and response.lower() != "no":
        response = input("Incorrect input, please only type 'yes' or 'no':  ")
    return response


def no_numeric_chars_check(response):
    if any(char.isdigit() for char in response) is False:
        new_response = input("Please only type letters, not numbers:  ")
    return new_response

def no_letters_check(response):
    check = response.isnumeric()
    if check is True:
        return response
    new_response = response
    while new_response.isnumeric() is False:
        new_response = input("Please only type numbers, not letters:  ")
    return new_response


def response_on_list_check(response, list):
    on_list = False

    for x in list:
        if x.lower() == response.lower():
            response = response.lower()
            return response

    while on_list is False:
        response = input("Choice not available, please type one of the options above:  ")
        for x in list:
            if x.lower() == response.lower():
                on_list = True
        response = response.lower()
    return response