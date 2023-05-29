def IBAN_address_input():
    IBAN_address = input("Please enter your IBAN number: ")
    iban_no_spaces = IBAN_address.replace(" ", "") # Removing spaces
    valid_check(iban_no_spaces)
    

def valid_check(iban_no_spaces):
    if len(iban_no_spaces) >= 18: # Checks if username length matches 18
        iban_country_code = iban_no_spaces[4:] + iban_no_spaces[:4]
        
        #print(iban_country_code)
        iban_numbers = iban_country_code.replace("FI", "1518")
        iban_numbers_int = int(iban_numbers)
        # Results of upper should be 50001510000023FI42
        if iban_numbers_int % 97 == 1:
            print(True, "Valid IBAN")
        else:
            print(False, "Invalid IBAN")

IBAN_address_input()
