from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    def isValid(word, hand, wordList):
        """
        Returns True if word is in the wordList and is entirely
        composed of letters in the hand. Otherwise, returns False.

        Does not mutate hand or wordList.
       
        word: string
        hand: dictionary (string -> int)
        wordList: list of lowercase strings
        """
        tempHand = hand.copy()
        for letter in word:
            check = tempHand.get(letter, 0)
            if check == 0:
                return False
            else:
                tempHand[letter] -= 1
        return True

    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Create a new variable to store the maximum score seen so far (initially 0)
    max_score = 0
    # Create a new variable to store the best word seen so far (initially None)  
    best_word = None
    ### letterStr = ''.join(list(k*v for k, v in hand.iteritems()))
    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isValid(word, hand, wordList) == True:
            # Find out how much making that word is worth
            score = getWordScore(word, n)
            # If the score for that word is higher than your best score
            if score > max_score:
                # Update your best score, and best word accordingly
                max_score = score
                best_word = word
    if best_word == None:
        return None
    else:
        return best_word
    # return the best word you found.


#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    score = 0
    tempHand = hand.copy()
    
    while calculateHandlen(tempHand) > 0:
        print('Current hand:'),
        displayHand(tempHand)
        if compChooseWord(tempHand, wordList, n) == None:
            break
        else:    
            guess = compChooseWord(tempHand, wordList, n)
            wordScore = getWordScore(guess, n)
            score += int(wordScore)
            print('"' + str(guess) + '" earned ' + str(wordScore) + ' points. Total: ' + str(score))
            print
            tempHand = updateHand(tempHand, guess)

    print('Total score: ' + str(score))
    print
    
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    # TO DO... <-- Remove this comment when you code this function
    hand = {}
    while len(hand) >= 0:
        choice = raw_input('Enter "n" to deal a new hand, "r" to replay the last hand, or "e" to end game: ')
        if choice == 'e':
            break
        elif choice == 'r' and len(hand) < 1:
            print('You have not played a hand yet. Please play a new hand first!')
            print
        elif choice not in 'rne':
            print('Invalid command.')
        elif choice == 'r':
            x = 1
            while x > 0:
                choose = raw_input('Enter "u" to play a game, or "c" to watch the computer play: ')
                print
                if choose not in 'uc':
                    print('Invalid command.')               
                elif choose == 'c':
                    x -= 1
                    compPlayHand(hand, wordList, HAND_SIZE)
                elif choose == 'u':
                    x -= 1
                    playHand(hand, wordList, HAND_SIZE)
        elif choice == 'n':
            x = 1
            while x > 0:
                choose = raw_input('Enter "u" to play a game, or "c" to watch the computer play: ')
                print
                if choose not in 'uc':
                    print('Invalid command.')
                elif choose == 'c':
                    x -= 1
                    hand = dealHand(HAND_SIZE)
                    compPlayHand(hand, wordList, HAND_SIZE)
                elif choose == 'u':
                    x -= 1
                    hand = dealHand(HAND_SIZE)
                    playHand(hand, wordList, HAND_SIZE)
            
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


