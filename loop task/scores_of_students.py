# Define:
#
# A program that collect the scores of 15 students from the user
# Determine the passes and fail
#
# Understand:
# Collect scores or prompt the user to input the scores
# Sort ad the calculate the number of pass and fail using a pass mark of 45
# print the analytics on the console

pass_mark = 45
pass_count = 0
count = 0
fail_count = 0

for count in range (1, 16):
    student_score = int(input("Enter Score for Student "))
    if(student_score >= 45):
        pass_count += 1
       
        print("Pass ", pass_count)
    else:
        fail_count += 1
        print("Fail", fail_count)
        
if(student_score >= pass_mark):
    print("The number of passes is ", pass_count)
    print("The Number of fails is ", fail_count )
#
#print(count)
#    
