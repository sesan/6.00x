def gcdRecur(a, b):
    lo = min(a,b)
    hi = max(a,b)
    
    if lo == 0:
        return hi
    else:
        return gcdRecur(lo, hi%lo)

