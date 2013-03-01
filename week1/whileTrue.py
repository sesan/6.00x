x = int(raw_input("Enter an number to find it's square root: "))
epsilon = 0.01
step = 0.1
guess = 0.0
guesses = 0

while abs(guess**2-x) >= epsilon:
    if guess <= x:
        guess += step
        guesses += 1
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded in (' + str(guesses) + ' guesses): ' + str(guess))