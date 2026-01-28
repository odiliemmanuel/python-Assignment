#
#def string_confirm(word):
#    for count in range(len(str(word))):
#        if(count >= 2):
#            great = word[0] + word[1] + word[-2] + word[-1]
#            return great
#        elif(count == 1):
#            less = word[0] + word[1] + word[-2] + word[-1]
#            return less
#    return [""]
#        
#
#print(string_confirm("o"))

#def string_addition(comment):
#    adding = "ly"
#    lessy = "ing"
#    for element in range(len(str(comment))):
#        if(element > 2 and comment[-3] + comment[-2] + comment[-1] == comment[-3] + comment[-2] + comment[-1]):
#            return comment + adding
#       
#        if(element >= 2 and comment[-3] + comment[-2] + comment[-1] != lessy):
#            return comment + lessy


#print(string_addition("String"))
            

#def separate_odd_indexes(word):
#    results=""
#    for elements in range (len(word)):
#        if(elements % 2 != 0):
#            results += word[elements]
#    return results
#
#print(separate_odd_indexes("semicolon"))
#



#def largest_numbers(numbers):
#   new_list = []
#   largest = 0 
#   for count in numbers:
#        if count > largest: 
#            largest = count
#                
#   return largest
#print(largest_numbers([1, 6, 4, 34]))
#



#def largest_numbers(numbers):
#   new_list = []
#   smallest = numbers[0]
#   for count in numbers:
#        if count < smallest: 
#            smallest = count
#                
#   return smallest
#print(largest_numbers([1, 6, 4, 34]))


#def multiply_strings(word, number):
#    if type(number) == float:
#        return word
#    else:
#        result = word * number
#        return result
#
#print(multiply_strings("hello", 4))


def square_numbers(numbers):
    digit = []
    for count in numbers:
        number[count] **= 2
        digit.append(number)
        return digit

print(square_numbers([2, 4, 7]))


    






















    
        
