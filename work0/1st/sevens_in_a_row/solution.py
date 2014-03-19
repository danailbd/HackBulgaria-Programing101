def sevens_in_a_row(arr, n):
    sevens = 0
    for item in arr:
        if( item == 7 ):
            sevens += 1
    return sevens>n
