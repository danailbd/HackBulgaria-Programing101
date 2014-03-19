def is_decreasing(seq):
    if( len(seq) <= 1): return True
    if( seq[0] < seq[1]): return False
    return is_decreasing(seq[1:])
