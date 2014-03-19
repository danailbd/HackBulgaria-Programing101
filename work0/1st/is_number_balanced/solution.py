def is_number_balanced(n):
    if( n>0 and n<10 ):
        return True
    
    digs = digit_count(n)
    left = 0
    right = 0
    for i in range(0 ,digs//2):
        left += n//(10**i)%10
        right += n//(10**(digs-i-1))%10
    return left == right
