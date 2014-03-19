def is_int_palindrom(n):
    dig_count = digit_count(n)
    for i in range(0, dig_count//2):
        if( (n//(10**i))%10 == (n//(10**(dig_count-i-1)))%10 ):
            return True
        else:
            return False
