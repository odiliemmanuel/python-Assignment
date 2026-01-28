import random

maximum = 20

minimum = 0

number = 0

random_number = random.random(..., 1 - 20)
#random(1,20)

#number = int(input("Guess my number"))
   
while(number  != random_number):
    number = int(input("Guess my number "))

    if(number  > random_number):
        print("Too high, please try again")
         
    if(number  < random_number):
        print("Too low, please try again")
        
    if(number  == random_number):
        print("Correct guess")
        
    
      

   
