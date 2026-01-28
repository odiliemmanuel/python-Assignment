number = int(input("Enter a positive number "))
division = number // number
        
if(division != 1):
    print( number , " is not a prime number")
    
elif number % 2 == 0:
    print(number , " is not a prime number, it is even")
    
else:
    print(number, " is a prime number")
        
        
   
