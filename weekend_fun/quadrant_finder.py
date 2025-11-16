first_integer = float(input("Enter value for first Integer "))

second_integer = float(input("Enter value for second Integer "))

if(first_integer > 0 and second_integer > 0):
    print("Q1")

if(first_integer < 0 and second_integer > 0):
    print("Q2")

if(first_integer < 0 and second_integer < 0):
    print("Q3")

if(first_integer > 0 and second_integer < 0):
    print("Q4")

if(first_integer == 0 and second_integer == 0):
    print("Origin")

if(first_integer != 0 and second_integer == 0):
    print("X-axis")

if(first_integer == 0 and second_integer != 0):
    print("Y-axis")

