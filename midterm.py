def isMyNumber(guess):
    '''
    Procedure that hides a secret number. 
     It takes as a parameter one number and returns:
     *  -1 if the number is less than the secret number
     *  0 if the number is equal to the secret number
     *  1 if the number is greater than the secret number
    '''
    secret = 89739
    if guess > secret:
            return 1
    elif guess < secret:
            return -1
    elif guess == secret:
            return 0

def jumpAndBackpedal():
    '''
    isMyNumber: Procedure that hides a secret number. 
     It takes as a parameter one number and returns:
     *  -1 if the number is less than the secret number
     *  0 if the number is equal to the secret number
     *  1 if the number is greater than the secret number
 
    returns: integer, the secret number
    '''
    guess = 1
    if isMyNumber(guess) == 0:
        return guess
    foundNumber = False
    while not foundNumber:
        sign = isMyNumber(guess)
        if sign == -1:
            guess += 1
        elif sign == 1:
            guess -= 1
        else:
            foundNumber = True
    return guess        

##def jumpAndBackpedal():
##    '''
##    returns: integer, the secret number
##    '''
##    guess = 1
##    if isMyNumber(guess) == 0:
##        return guess
##    elif isMyNumber(guess) == -1:
##        return jumpAndBackpedal(guess + 1)
##    elif isMyNumber(guess) == 1:
##        return jumpAndBackpedal(guess - 1)


##def jumpAndBackpedal():
##    '''
##    isMyNumber: Procedure that hides a secret number. 
##     It takes as a parameter one number and returns:
##     *  -1 if the number is less than the secret number
##     *  0 if the number is equal to the secret number
##     *  1 if the number is greater than the secret number
## 
##    returns: integer, the secret number
##    '''
##    guess = 1
##    while True:
##        if isMyNumber(guess) == 0:
##            return guess
##        elif isMyNumber(guess) == -1:
##            guess += 1
##        elif isMyNumber(guess) == 1:
##            guess -= 1

##def jumpAndBackpedal(num):
##    '''
##    isMyNumber: Procedure that hides a secret number. 
##     It takes as a parameter one number and returns:
##     *  -1 if the number is less than the secret number
##     *  0 if the number is equal to the secret number
##     *  1 if the number is greater than the secret number
## 
##    returns: integer, the secret number
##    ''' 
##    guess = num
##    if isMyNumber(guess) == 0:
##        return guess
##    while True:
##        sign = isMyNumber(guess)
##        if sign == -1:
##            guess += 1
##        elif sign == 0:
##            return guess
##        elif sign == 1:
##            guess -= 1


def generateForm(story, listOfAdjs, listOfNouns, listOfVerbs):
    """ 
    story: a string containing sentences
    listOfAdjs: a list of valid adjectives
    listOfNouns: a list of valid nouns
    listOfVerbs: a list of valid verbs

    For each word in story that is in one of the lists,
    * replace it with the string '[ADJ]' if the word is in listOfAdjs
    * replace it with the string '[VERB]' if the word is in listOfVerbs
    * replace it with the string '[NOUN]' if the word is in listOfNouns

    returns: string, A Mad-Libs form of the story. 
    """
    new_story = []
    story_list = story.split(' ')
    for word in story_list:
        if word in listOfAdjs:
            new_story.append('[ADJ]')
        elif word in listOfNouns:
            new_story.append('[NOUN]')
        elif word in listOfVerbs:
            new_story.append('[VERB]')
        else:
            new_story.append(word)
    return ' '.join(new_story)

def generateTemplates(madLibsForm):
    """ 
    madLibsForm: string, in a Mad-Lib form. See output of `generateForm`

    returns: a list of '[ADJ]', '[VERB]', and '[NOUN]' strings, in
    the order they appear in the madLibsForm.             
    """
    mad_list = madLibsForm.split(' ')
    mad_temp = []
    mad_parts = ['[ADJ]', '[NOUN]', '[VERB]']
    for word in mad_list:
        if word in mad_parts:
            mad_temp.append(word)
    return mad_temp

def verifyWord(userWord, madTemplate, listOfAdjs, listOfNouns, listOfVerbs):
    """ 
    userWord: a string, the word the user inputted
    madTemplate: string, the type of word the user was supposed to input
    listOfAdjs: a list of valid adjectives
    listOfNouns: a list of valid nouns
    listOfVerbs: a list of valid verbs):

    returns: Boolean, whether or not the word is valid
    """
    if userWord in listOfAdjs and madTemplate == '[ADJ]':
        return True
    elif userWord in listOfNouns and madTemplate == '[NOUN]':
        return True
    elif userWord in listOfVerbs and madTemplate == '[VERB]':
        return True
    return False


def numPensRecur(n):
    """
    n is a non-negative integer

    Returns True if some non-negative integer combination of 5, 8 and 24 equals n
    Otherwise returns False.
    """
    a, b = 5, 8                  # 8 is a multiple of 24, so (in this case) we can ignore it
    
    if n < a:                    # failing base case: we can't buy less than 5 pens, so return False
        return False
    elif n%a == 0 or n%b == 0:   # passing base case: check if a or b are perfect divisors of n
        return True
    else:
        return numPensRecur(n-a)      # could/shoud be 'return numPens(n-a) or return numPens(n-b)' but base case tests for either


def numPensIter(n):
    a, b = 5, 8
    
    while n > 0:
        if n < 5:
            return False
        elif n%a == 0 or n%b == 0:
            return True
        n -= a



#### TESTS ####
print "jumpAndBackpedal secret number:", jumpAndBackpedal()

madTemplate = generateTemplates('At the [ADJ] thrift [NOUN] I [VERB] a pair of [ADJ] [NOUN] that [VERB] like [NOUN] your [NOUN] might wear')

story = 'The ravenous zombies started attacking yesterday'
listOfAdjs = ['ravenous']
listOfNouns = ['zombies', 'humans', 'yesterday']
listOfVerbs = ['attacking', 'attacks']
print generateForm(story, listOfAdjs, listOfNouns, listOfVerbs)

story = 'At the creepy thrift store I found a pair of plaid pants that looked like something your grandpa might wear'
listOfAdjs = ['creepy', 'plaid']
listOfNouns = ['store', 'pants', 'something', 'grandpa']
listOfVerbs = ['found', 'looked']
userWord = 'creepy'

print(verifyWord(userWord, madTemplate, listOfAdjs, listOfNouns, listOfVerbs))
print generateForm(story, listOfAdjs, listOfNouns, listOfVerbs)
        
def testNumPensRecur():
    ans = []
    for i in range(5, 100):
        if numPensRecur(i):
            ans.append(i)
    return ans

def testNumPensIter():
    ans = []
    for i in range(5, 100):
        if numPensIter(i):
            ans.append(i)
    return ans


print "Recursive:", testNumPensRecur()
print "Iterative:", testNumPensIter()
