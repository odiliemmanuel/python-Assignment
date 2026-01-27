def sum_numbers_in_a_list():
    my_list = [3,5,6,7,4]
    sum_of_elements = 0
    for element in my_list:
       sum_of_elements += element

    return sum_of_elements        


def calculate_length_of_element_and_output_length():
    new_list = []
    my_list = ["eat", "play", "bark", "chop", "sapa"]
    for element in my_list:
        new_list.append(len(element))
    return new_list    


def output_odd_indexes():
    my_list = [5,8,7,9,3,2,1]
    for count in range(len(my_list)):
        if(count % 2 != 0):
            print(my_list[count])




def sort_array_of_element_by_size():
    my_list = ["eat", "playing", "choppy", "throw"]
    new_list = []
    for count in range(len(my_list)):
        for index in range(len(my_list)):
            if(len(my_list[index]) > len(my_list[count])):
                swap = my_list[count]
                my_list[count] = my_list[index]
                my_list[index] = swap
    return my_list
                
        





def output_the_length_of_elements_and_its_index():
    my_list = sort_array_of_element_by_size()
    for index, element in enumerate(my_list):
        print((index + 1), ": ", element)




output_the_length_of_elements_and_its_index()
#print(my_list)
























