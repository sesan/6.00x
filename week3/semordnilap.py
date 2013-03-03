def semordnilapWrapper(str1, str2):
    # A single-length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False

    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False

    return semordnilap(str1, str2)

def semordnilap(str1, str2):
    # first, reverse str2. Then, make sure str1 and str2 are the same length.
    switch = str2[::-1]

    # Then we check if the two strings are the same length AND
    # check if (first char of str1) == (first char of reversed str2)

    if len(str1) != len(switch) or str1[0] != switch[0]:
        return False
    
    # The recursive call shortens both strings by one char and returns True
    # if they all match up after each iteration
    
    else:
        return True or semordnilap(str1[1:], switch[1:])
