def isVowel(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    char = char.lower()
    if char in ['a', 'e', 'i', 'o', 'u']:
    	return True
