def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    result = base
    
    if exp == 0:
        return float(1.0000)
    else:
        while exp > 1:
            result = result * base
            exp -= 1
        return result
