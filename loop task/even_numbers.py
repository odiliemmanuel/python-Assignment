# Define:
#
# A program that that collects even numbers
# And prints in a straight line
#
# Understand:
#
# Calculate for even numbers between 1 to 100
# Collect them
# Print or display in the console

for count in range (1, 101):
    if(count % 2 == 0):
        print(count, end=" ")
        continue
