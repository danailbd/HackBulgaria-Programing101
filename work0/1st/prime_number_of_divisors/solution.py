def prime_number_of_divisors(n):
    result = n
    div = n//2
    while div>0:
        if( n%div == 0 ):
            result += 1
        div -= 1
    return is_prime(result)
