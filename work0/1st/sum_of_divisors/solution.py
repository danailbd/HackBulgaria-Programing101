def sum_of_divisors(n):
    result = n
    div = n//2
    while div>0:
        if( n%div == 0 ):
            result += div
        div -= 1
    return result
