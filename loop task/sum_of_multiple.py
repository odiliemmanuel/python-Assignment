# Define:
#
# A program that calulates the multiples of ten
# And prints their sum
# Breakdown:
#
# collect multiples of ten
# sum them up by adding each of the sum together
# prints the total sum of multiples


suming = 0

for number in range (10, 200001,10):
    suming += number
print("The sum of multiples of 10 is ", suming)
 
