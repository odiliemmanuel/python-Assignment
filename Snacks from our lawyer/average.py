def average_of_a_list(count):
    numbers_in_list = [10, 20, 30, 40, 50]
    average_of_list = 0
    total_lenght = 0
    for count in numbers_in_list:
        total_lenght += 1
        sum_of_list = 0
        for index in numbers_in_list:
            sum_of_list += index
            average_of_list = sum_of_list / total_lenght
    return (int(average_of_list))

print(average_of_a_list([10, 20, 30, 40, 50]))
