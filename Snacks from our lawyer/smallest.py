def smallest_element_in_a_list(count):
    numbers = [10, 30, 40, 50, 70, 90, 20]
    smallest_element = numbers[1]
    for count in numbers:
        if count < smallest_element:
            smallest_element = count
    return smallest_element

print(smallest_element_in_a_list([10, 30, 40, 50, 70, 90, 20]))
