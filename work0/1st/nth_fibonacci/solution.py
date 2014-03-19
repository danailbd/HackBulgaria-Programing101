def nth_fibonacci(n):
    first = 1
    second = 1
    while n>1:
        second += first
        first = second-first
        n -= 1
        
    return first
