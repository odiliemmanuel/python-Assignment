condition = "No"

answer = " "

count_positive = 0

count_negative = 0

count_zero = 0
    
while (condition is not equals(answer)):

    number = int(input("Enter any number "))

if(number > 0):
    count_positive ++
        
elif (number < 0):
    count_negative ++

else:
     count_zero ++
        
print("Do you want to continue, enter(Yes or No) ")

answer = input.next()
        
print("The count of Positive numbers is ", count_positive)

print("The count of Negative numbers is ", count_negative)

print("The count of Zero numbers is ",  count_zero)
        
