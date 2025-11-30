def odd_numbers_in_list(count):
    numbers_in_list = [10, 20, 30, 40, 50, 60, 70, 80]
    for number in numbers_in_list:
        count = 0
        if(number % 20 == 0):
            count += number
        return count

print(odd_numbers_in_list([10, 20, 30, 40, 50, 60, 70, 80]))
