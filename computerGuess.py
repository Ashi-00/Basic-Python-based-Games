#ComputerGuess GAME
# The user would think of a number b/w 1 to x and let the computer guess it by dropping hints that the number guessed by computer
#is lower/higher or the correct number itself!

import random
def compGuess(x):
    low=1
    high=x

    feedback=''
    
    while (feedback != 'c'):
        if high != low:
            guess=random.randint(low,high)
        else:
            guess=low   #or high as low==high which means same number hence that would be the answer.
        feedback=input(f"If {guess} is too high then (H), too low then (L) OR correct then(c)").lower()
        print()
        if feedback== 'h':
            high=guess-1
        elif feedback == 'l':
            low=guess+1
    print(f"Congratss! the computer guessd it right!!..it was {guess}")
    print()

x=10
compGuess(x)




