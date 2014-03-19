def count_vowels(str):
    result = 0
    for item in str:
        if( item.lower() in "aeiouy" ):
            result += 1
    return result
