#Russain roulet dice game

import random

print ("Russain Roulet Dice Game, Die If You Get 0.(Enter = Roll)")


phrases = ["There you go!", "Keep up the good work.", "Keep it up.", "Good job.",
           "I’m so proud of you!", "Hang in there.", "Don’t give up.", "Keep pushing.",
           "Keep fighting!", "Stay strong.", "Never give up.", "Come on! You can do it!",
           "I’m behind you 100%.", "Follow your dreams.", "Reach for the stars.",
           "Do the impossible.", "Believe in yourself.", "The sky is the limit."]


points = 0 + 1


"""random number between 0-6, print out phrases if number is 1-6"""

while not 0:
   ran_p = random.choice(phrases)
   dice = random.randint(0,6)
   roll = input(dice) 
   

   if dice == 1:
      print("%s " %(ran_p))
      points += 1
      
   elif dice == 2:
      print("%s " %(ran_p))
      points += 1
      
   elif dice == 3:
      print("%s " %(ran_p))
      points += 1
      
   elif dice == 4:
      print("%s " %(ran_p))
      points += 1
      
   elif dice == 5:
      print("%s " %(ran_p))
      points += 1
      
   elif dice == 6:
      print("%s " %(ran_p))
      points += 1
      
   if dice == 0:
      points - 1
      print("Game Over, You Die! " + "Total Points: " + str(points - 1))
      break



   
   

