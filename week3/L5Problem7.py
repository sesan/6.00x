def lenRecur(aStr):
    ans = 0
    if aStr == '':
        return ans
    else:
        ans += 1
        return ans + lenRecur(aStr[0:-1])
