def even_positions_in_list(count):
    sum = 0
    for elements in range(0, len(count), 2):
        sum += count[elements]
    return sum

print(even_positions_in_list([10, 20, 30, 40, 50, 60, 70, 80]))
