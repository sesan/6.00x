def gcdRecur(a, b):
    lo = min(a,b)
    hi = max(a,b)
<<<<<<< HEAD
    
    if lo == 0:
        return hi
    else:
        return gcdRecur(lo, hi%lo)
=======
    if hi%lo == 0 or lo <= 1:
        return lo
    else:
        return gcdRecur(hi, lo-1)
>>>>>>> 24c2642e6c67b9e90a6d3d874fb50322aaedc21d

