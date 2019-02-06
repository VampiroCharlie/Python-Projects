# basic cho-han dice game without points or complex features.
# room for improvements at later date.

import random

def Cho_Han():
   print ('Please Roll the Dice')

   cho = [2, 4, 6, 8, 10, 12]# values for odd and even
   han = [1, 3, 5, 7, 9, 11]


   cho_han = random.randint(1, 12)#random number choosen between 1-12
   guess = random.randint(1,12)#players random number

   print ('Your number is ' + str(guess))
   print ('The dealers number is ' + str(cho_han))


   """ Prints Cho or Han """

   if cho_han in cho:
       print ('Cho!')
   elif cho_han in han:
       print ('Han!')
   else:
       print ('Troubleshooting 1')



   """Determines Whether Player Has Won or Lost"""
   
   if guess in cho and cho_han in cho:# both player input and dice must be even or odd to win
       print ('Well Done Sir, You Win!')
   elif guess in han and cho_han in han:
       print ('Well Done Sir, You Win!')    
   else:
       print ('Unfortunately Sir You Lose, Would You Like To Play Again?')

   if guess == cho_han:#stament in case if player number and dice are same. 
       print('Wow You\'re Amazinig, You Got The Same Number')

Cho_Han()

