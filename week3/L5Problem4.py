def gcd(a, b):
    lo = min(a,b)
    hi = max(a,b)
    if hi%lo == 0 or lo <= 1:
        return round(lo)
    else:
        return gcd(hi, lo-1)

