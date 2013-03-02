def isIn(char, aStr):
    lowerStr = aStr.lower()
    ans = int(len(lowerStr)/2)
    if lowerStr == '':
        return False
    elif len(lowerStr) == 1:
        return char == lowerStr
    elif char == lowerStr[ans]:
        return True
    elif char < lowerStr[ans]:
        return isIn(char, lowerStr[:ans])
    elif char > lowerStr[ans]:
        return isIn(char, lowerStr[ans:])
