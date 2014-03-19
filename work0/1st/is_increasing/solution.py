def is_increasing(seq):
    if( len(seq) <= 1): return True
    if( seq[0] > seq[1]): return False
    return is_increasing(seq[1:])
