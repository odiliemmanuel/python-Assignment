list_of_numbers = [2, 3, 4]

square = 0

cube = 0 

for character in list_of_numbers:
    square = int(character ** 2)
    cube = int(character ** 3)   
    list_of_numbers = [character, square, cube]
    print (list_of_numbers, end= " ")
    
    


