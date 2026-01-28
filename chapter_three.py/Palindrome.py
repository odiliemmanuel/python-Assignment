number = int(input("Enter a Five Digit Number ") )

numberOne = number // 10000

numberTwo = numberOne  % 10 % 10

numberThree = number // 100 % 10 % 10

numberFour = number //10 % 10 % 10 % 10

numberFive = number % 10

print( numberFive, numberFour, numberThree, numberTwo, numberOne)
  
