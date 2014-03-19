def count_consonants(str):
    result = 0
    for item in str:
        if( item.lower() in "bcdfghjklmnpqrstvwxz" ):
            result += 1
    return result
