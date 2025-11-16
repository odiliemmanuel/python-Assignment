first_integer = int(input("Enter value for first Integer "))

second_integer = int(input("Enter value for second Integer "))

third_integer = int(input("Enter value for third Integer"))

largest = first_integer

if( second_integer > largest and second_integer > third_integer):
    print("The largest number is ", second_integer) 
 
if(third_integer > largest and third_integer > second_integer):
    print("The largest number is ", third_integer)




