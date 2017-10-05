import re

def validate_email(email):
    try:
        if re.fullmatch("[a-zA-Z0-9]+@[a-zA-Z0-9]+(\.[a-zA-Z0-9]+){1,}", email):
            return True
    except Exception as e:
        print("ERROR: ", e)
    return False

#test output
print(validate_email('piotr@dyba.com.pl'))
print(validate_email('piotrdyba.com.pl'))
print(validate_email('piotr@dyba'))


#postcode
def validate_zip(zip):
    try:
        if re.fullmatch("([0-9]){2}-([0-9]){3}", zip):
            return True
    except Exception as e:
        print("ERROR: ", e)
    return False


#test output
print(validate_zip('12-345'))
print(validate_zip('12345'))
print(validate_zip('1233-3345'))