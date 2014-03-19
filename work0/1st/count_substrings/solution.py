def count_substrings(haystack, needle):
    if( haystack == '' ): return 0
    if( haystack[0] == needle[0] ): 
        if( haystack[0:len(needle)] == needle ):
            return 1 + count_substrings( haystack[len(needle):], needle )
    return count_substrings( haystack[1:], needle )
