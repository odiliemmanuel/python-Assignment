import random

def get_suggestion(my_list):
    pages = random.randint(1,1)
    book_suggestion = my_list[pages]
    return book_suggestion[0]

def remove_book(my_list, book):
    my_list.remove(book)
    return my_list

def add_book(my_list, book):
    my_list.append(book)
    return my_list

def update_book(my_list, old_book, new_book):
    index = my_list.index(old_book)
    my_list[index] = new_book
    return my_list

def show_all_books(my_list):
    return my_list
