def list_to_number(digits):
    result = 0
    for i in range(0, len(digits)):
        result += digits[i]*(10**(len(digits)-i-1))
    return result
