def lenIter(aStr):
    ans = 0
    assert type(aStr) == str
    for c in aStr:
        ans += 1
    if ans < 1:
        return 0
    elif ans > 0:
        return ans
    
