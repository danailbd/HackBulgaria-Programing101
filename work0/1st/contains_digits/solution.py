def contains_digits(number, digits):
    for item in digits:
        if( contains_digit(number, item) == False ):
            return False
    return True
