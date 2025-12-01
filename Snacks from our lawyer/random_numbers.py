import random

def generating_random_numbers(count): 

    number_list = []

    for count in range(10):

        random_numbers = random.randint(1, 101)

        return random_numbers

print(generating_random_numbers(10))
