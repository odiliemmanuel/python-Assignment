total_bill = float(input("How much is your your bill "))

is_member = str(input("Are you a member "))

if(total_bill >= 1000 and is_member == "yes"):
    print("10% off")

elif(total_bill >= 1000 and is_member != "yes"):
    print("5% off")

else:
    print("No discount")
    
    
