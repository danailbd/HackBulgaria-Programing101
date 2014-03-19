def is_prime(n):
    if( n<0 ):
        return False
    else:
        if ( sum_of_divisors(n) > 1+n ):
            return False
        return True
