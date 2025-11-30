def largest_number_in_a_list(count):
    numbers = [10, 20, 30, 40, 50]
    largest_element = numbers[0]
    for count in numbers:
        if count > largest_element:
            largest_element = count
    return largest_element

print(largest_number_in_a_list([10, 20, 30, 40, 50]))
