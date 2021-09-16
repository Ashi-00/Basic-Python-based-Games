#GAME TIME -->>  HIGH LOW 
import random
def guess(x):
    hidden=random.randint(1,x)
    
    n=0  #intialising with a number thats out of the ranges so that the loop can begin since loop welcomes a number!=hidden
    
    while (n != hidden):
        n=int(input(f"Enter a number between 1 and {x} = "))
        if  hidden-10<=n<hidden:
            print("Ah! guess again that was a little LOW")
            print()
        elif hidden<n<=hidden+10:
            print("Ah! guess again that was a little HIGH")
            print()
        elif 1<=n<hidden-10:
            print("Oops! guess again that was is too LOW!")
            print()
        elif x>=n>hidden+10:
            print("Oops! guess again that was too HIGH!")
            print()
    
    print(f"CONGRATS!..you got it..the number was {hidden}")
    print()

        
x=100     #UPPER LIMIT
guess(x)
