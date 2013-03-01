def isVowel2(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    char = char.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    if char in vowels:
        return True
    else:
        return False
