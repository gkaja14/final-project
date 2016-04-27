import random
def getSecretNum(NumDigits):
    # numbers = random.randint(1, 10)
    numbers = list(range(10))
    random.shuffle(numbers)
    

    
    secretNum=''
    for i in range (numDigits):
        secretNum +=str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    if guess == secretNum:
        return 'You got it!'

    clue = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clue.append('Fermi')
        elif guess [i] in secretNum:
            clue.append('pico')
    if len(clue) == 0:
        return 'Bagels'
    clue.sort()
    return''.join(clue)

def digitsOnly(num):
    if num == '':
        return False
    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False
    return True



def playAgain():
    print ('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')
    
    return input
numDigits = 3
MaxGuess = 10

print('I am thinking of a %s-digit number. Try to guess what it is.' % (numDigits))
print ('Here are some clues:')
print('When I say:         That means:')
print('Pico       One digit is correct but in the wrong position.')
print('Fermi      One digit is correct and in the right position.')
print('Bagels     No digit is correct.')

while True:
    secretNum = getSecretNum(numDigits)
    print('I am thinking of a number. you have %s guesses to get it.' %( MaxGuess ))

    numGuesses = 1
    while numGuesses <= MaxGuess:
        guess=''
        while len(guess) != numDigits or not digitsOnly(guess):
            print('Guess #%s: ' %(numGuesses))
            guess = (input())
                  

        clue=getClues(guess, secretNum)
        print(clue)
        numGuesses += 1

        if guess == secretNum:
            break

        if numGuesses > MaxGuess:
            print('You ran out of guesses. The answer was %s.' % (secretNum))

    if not playAgain():
        break
                
