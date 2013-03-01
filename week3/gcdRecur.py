def gcdRecur(a, b):
    lo = min(a,b)
    hi = max(a,b)
    if hi%lo == 0 or lo <= 1:
        return lo
    else:
        return gcdRecur(hi, lo-1)

