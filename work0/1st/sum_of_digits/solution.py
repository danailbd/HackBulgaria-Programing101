def sum_of_digits(n):
    result = 0
    while n>0:
        result += n%10
        n //= 10
    return result
