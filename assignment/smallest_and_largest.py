numberOne = int(input("Input first Digit Number "))

numberTwo = int(input("Input second Digit Number "))

numberThree = int(input("Input third Number "))

sumOfNumbers = numberOne +  numberTwo + numberThree
print("The Sum is", sumOfNumbers)

average = sumOfNumbers / 3
print("The Average is", average)

largest_number = 0

if(numberTwo > numberOne and numberTwo > numberThree):
    largest_num = numberTwo
    print("The largest number is", largest_num)

if(numberThree > numberOne and numberThree > numberTwo):
    largest_num = numberThree
    print("The largest number is", largest_num)

if(numberOne > numberTwo and numberOne > numberThree):
    largest_num = numberOne
    print("The largest number is", largest_num)


smallest_number = 0


if(numberTwo < largest_num):
    smallest_number = numberTwo
    print("The smallest number is", smallest_number)

elif(numberThree < numberOne and numberThree < numberTwo):
    smallest_number = numberThree
    print("The smallest number is", smallest_number)

elif(numberOne < numberTwo and numberOne < numberThree):
    smallest_number = numberOne
    print("The smallest number is", smallest_number)

