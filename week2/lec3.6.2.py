# lecture 3.6, slide 2
# bisection search for square root
import math

print("Please think of a number between 0-100!")
low = 0
high = 100
numGuesses = 0
guess = math.floor((high + low)/2)
while True:
	print('Is your secret number ' + str(guess) + '?')
	x = str(raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly: "))

	if x == 'c':
		isTrue = True
		break
	elif x == 'h':
		high = guess
		guess = math.floor((high + low)/2)
		numGuesses += 1
	elif x == 'l':
		low = guess
		guess = math.floor((high + low)/2)
		numGuesses += 1
	elif x not in ['c','h', 'l']:
		print('Sorry, I did not understand your input.')
if isTrue == True:
	print("Game over. Your secret number was: " + str(guess))

