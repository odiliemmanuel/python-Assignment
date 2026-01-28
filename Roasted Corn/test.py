my_lists = [1, 4, 3, 2, 7, 8, 5, 13, 11]

def odd_numbers(element):
    return element % 2 != 0
print(list(filter(odd_numbers,my_lists)))
