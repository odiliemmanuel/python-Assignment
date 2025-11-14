# a program that calculates the average of three scores
# prompt the user to enter scores
# store as variable
# if score is less than 90 and less than 100 print A
#if scores is less than 80 and less than 90 print B
# if scores is less than 70 and less than 80 print C
# if scores is less than 60 and less than 70 print D
# if scores is less than 0 and less than 60 print F



scoreOne = int(input("Enter the First score"))

scoreTwo = int(input("Enter the Second Score"))

scoreThree = int(input("Enter the Third Score"))

if(scoreOne and scoreTwo and scoreThree < 0 ):
    print("Invalid Input")

average = scoreOne + scoreTwo + scoreThree // 3

if(average <= 90 and average <= 100):
    print("A")

if(average <= 80 and average < 90):
    print("B")

if(average <= 70 and average < 80):
    print("C")

if(average <= 60 and average < 70):
    print("D")

if(average <= 0 and average < 60):
    print("F")
