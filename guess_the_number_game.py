#guess the number game

import random



num = random.randint(1, 11) # random number between 1 and 10
lives = 3 # number of lives

print("I'm Thinking of a Number Between 1 and 10, You have %d Lives! " % (lives))

guess = input("Try To Guess My Number! ") # player inputs number



""" print guess: high or low, and then continues loop, until lives run out or player wins"""

while guess != num:
    
    
    if int(guess) > int(num):
        print("Your Number is Too High, Keep Trying!")
        lives -=1  
    
    elif int(guess) < int(num):
        print("Your Number is Too Low, Keep Trying!")
        lives -=1
        
        
    elif int(guess) == int(num):
        print("Well Done You Win, You Had %d Live Left!" %(lives))
        break
    else:
        print("Troubleshooting 1")


    if int(lives) == 0:
        print("You've Run out of Lives, You Lose!")
        break

    guess = input("Try To Guess My Number! ")
