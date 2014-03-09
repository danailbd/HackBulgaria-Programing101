def nth_fibonacci(n):
    first = 1
    second = 1
    while n>1:
        second += first
        first = second-first
        n -= 1
        
    return first

def sum_of_digits(n):
    result = 0
    while n>0:
        result += n%10
        n //= 10
    return result

def sum_of_min_and_max(arr):
    return min(arr)+max(arr)

def sum_of_divisors(n):
    result = n
    div = n//2
    while div>0:
        if( n%div == 0 ):
            result += div
        div -= 1
    return result

def is_prime(n):
    if( n<0 ):
        return False
    else:
        if ( sum_of_divisors(n) > 1+n ):
            return False
        return True

def prime_number_of_divisors(n):
    result = n
    div = n//2
    while div>0:
        if( n%div == 0 ):
            result += 1
        div -= 1
    return is_prime(result)

def sevens_in_a_row(arr, n):
    sevens = 0
    for item in arr:
        if( item == 7 ):
            sevens += 1
    return sevens>n

#Problem 7
def digit_count(n):
    result = 0
    while n>0:
        result += 1
        n //= 10
    return result

def is_int_palindrom(n):
    dig_count = digit_count(n)
    for i in range(0, dig_count//2):
        if( (n//(10**i))%10 == (n//(10**(dig_count-i-1)))%10 ):
            return True
        else:
            return False

#Problem 8
def contains_digit(number, digit):
    while number>0: 
        if( number%10 == digit ):
            return True
        number //= 10
    return False

#Problem 9
def contains_digits(number, digits):
    for item in digits:
        if( contains_digit(number, item) == False ):
            return False
    return True

#Problem 10
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

#Problem 11
def count_substrings(haystack, needle):
    if( haystack == '' ): return 0
    if( haystack[0] == needle[0] ): 
        if( haystack[0:len(needle)] == needle ):
            return 1 + count_substrings( haystack[len(needle):], needle )
    return count_substrings( haystack[1:], needle )

#Problem 12
def count_vowels(str):
    result = 0
    for item in str:
        if( item.lower() in "aeiouy" ):
            result += 1
    return result

#Problem 13
def count_consonants(str):
    result = 0
    for item in str:
        if( item.lower() in "bcdfghjklmnpqrstvwxz" ):
            result += 1
    return result

#Problem 14
def number_to_list(n):
    list = []
    while n>0:
        list.append(n%10)
        n //= 10
    list.reverse()
    return list

#Problem 15
def list_to_number(digits):
    result = 0
    for i in range(0, len(digits)):
        result += digits[i]*(10**(len(digits)-i-1))
    return result

#Problem 16
def biggest_difference(arr):
    return min(arr)-max(arr)

#Problem 17
def slope_style_score(scores):
    result = 0
    for i in scores:
        result += i
    result -= (max(scores)+min(scores))
    return round(result/(len(scores)-2), 2)

#Problem 18
def is_increasing(seq):
    if( len(seq) <= 1): return True
    if( seq[0] > seq[1]): return False
    return is_increasing(seq[1:])

#Problem 19
def is_decreasing(seq):
    if( len(seq) <= 1): return True
    if( seq[0] < seq[1]): return False
    return is_decreasing(seq[1:])

#Problem 20
def what_is_my_sign(day, month):
    signs = { "Aquarius": [21,1], "Pisces": [20,2], "Aries": [21,3], "Taurus":[21,4], "Gemini": [22,5], "Cancer": [22,6], "Leo": [23,6], "Virgo": [23,8], "Libra": [24,9], "Scorpio": [24,10], "Sagittarius": [23,11], "Capricorn": [22,12]}
    for sign in signs:
        if( signs[sign][1] == month and signs[sign][0] < day or
            signs[sign][1] == month+1 and signs[sign][0] > day ):
            return sign

#Problem 21
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

#Problem 22
def calculate_coins(sum):
    result = {1:0 ,2:0 ,5:0 ,10:0 ,50:0 ,20:0}
    sum *= 100 #makes the sum to stotinki
    for coin in [50,20,10,5,2,1]:
        result[coin] += sum//coin
        sum %= coin
    return result

def main():
    print(is_increasing([1,2,3,4,5]));
    print(calculate_coins(0.53))


if __name__ == '__main__':
    main()
