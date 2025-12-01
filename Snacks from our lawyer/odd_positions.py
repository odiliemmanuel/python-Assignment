def odd_numbers_in_list(count):
    sum = 0
    for element in range(1, len(count), 2):
        sum += count[element];
    return sum

print(odd_numbers_in_list([10, 20, 30, 40, 50, 60, 70, 80]))
