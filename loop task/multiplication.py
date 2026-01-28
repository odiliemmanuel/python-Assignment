# Define:
#
# A program that prints a multiplication table of any number
# And print or display in the console
# Understand:
#
# Collect an integer from the user or prompt the user to enter an integer
# Calculate the product of that integer with numbers one to ten using a loop
# Print the result on the console

number = int(input("Enter an integer number"))

product = 0

for count in range (1,11):
    product = number * count
    print(number, " * \t", count, " =\t ", product)
