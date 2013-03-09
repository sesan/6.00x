# 6.00x Problem Set 5
#
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    coderRef = dict()
    coderUpp = dict()
    coderDict = dict()
    build = 1
    if shift <= 26 and shift >= 0:
        for char in string.ascii_lowercase:
            coderDict[char] = build
            coderRef[build] = char
            build += 1
        if len(coderDict) < 26:
            print 'Error building base dictionary (too few items)'
        elif len(coderDict) > 26:
            print 'Error building base dictionary (too many items)'
        else:
            for k, v in coderDict.iteritems():
                if v + shift > 26:
                    coderDict[k] = coderRef[v - 26 + shift]
                    coderUpp[k.upper()] = coderRef[v - 26 + shift].upper()
                else:
                    coderDict[k] = coderRef[v + shift]
                    coderUpp[k.upper()] = coderRef[v + shift].upper()
            coderDict.update(coderUpp)
        return coderDict
    else:
        print('shift must be between 0 and 26')
        return None
    

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    punctNum = ''.join(string.punctuation) + ' ' + '0123456789'
    tempStr = str()
    coderKey = coder
    
    for char in text:
        if char in punctNum:
            tempStr = tempStr + char
        else:
            tempStr = tempStr + coderKey[char]
    return tempStr


def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    key = applyCoder(text, buildCoder(shift))
    return key

#
# Problem 2: Decryption
#
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    bestShift = int()
    count = 0
    bestCount = 0
    tempWords = ''
    tempWords2 = []
    for i in range(26):
        tempWords = applyShift(text, i)
        tempWords2 = tempWords.split(' ')
        for word in tempWords2:
            if isWord(wordList, word):
                count += 1
        if count > bestCount:
            bestShift = i
            bestCount = count
        count = 0
    return bestShift

    
def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
    wordList = loadWords()
    # remove .rstrip() when running in edX grader
    story = getStoryString().rstrip('\n')
    bestShift = findBestShift(wordList, story)
    return applyShift(story, bestShift)

#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    # To test findBestShift:
##    wordList = loadWords()
##    s = applyShift('Hello, world!', 8)
##    bestShift = findBestShift(wordList, "Ocz oZvxczm'n iVhz dN OVwdocV?")
##    assert applyShift(s, bestShift) == 'Hello, world!'
    # To test decryptStory, comment the above four lines and uncomment this line:
      decryptStory()
