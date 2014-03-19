def prime_factorization(n):
    
    if( is_prime(n) ): return [(n,1)]
    
    result = []
    divisor_count = 0
    iter = n//2
    while iter!=1:
        if(is_prime(iter) and n%iter == 0):
            divisor_count += 1
            n //= iter
        else:
            if( divisor_count>0 ):
                result.append((iter,divisor_count))
                divisor_count = 0
            iter -= 1
    result.reverse()
    return result
