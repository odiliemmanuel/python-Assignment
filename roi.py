# A program that asks the user for investment amount
# Prompt the user to enter the number of years
# store in a variable
# Prompt the user to enter interest rate
# store in a variable
# Calculate the ROI and print result in a tabular form
#


investment_amount = int(input("Enter Your investment Amount "))

year = int(input("Enter Number of Years "))

interest_rate = int(input("Enter Interest Rate "))

interest = (interest_rate/100)





print(f"{'Year' :<10}{'Interest Rate':<15}{'ROI':<30} ")

for number in range (0,year):
    investment_amount += (interest * investment_amount )
    print(f"{year :<10}{interest:<15}{investment_amount:<30} ")

        
        





