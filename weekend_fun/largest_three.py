first_integer = int(input("Enter value for first Integer "))

second_integer = int(input("Enter value for second Integer "))

third_integer = int(input("Enter value for third Integer"))

largest = first_integer

if( second_integer > largest ):
    largest = second_integer

 
if(third_integer > largest ):
    largest = third_integer

print("The largest number is ", largest) 

