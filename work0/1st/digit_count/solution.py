def digit_count(n):
    result = 0
    while n>0:
        result += 1
        n //= 10
    return result
