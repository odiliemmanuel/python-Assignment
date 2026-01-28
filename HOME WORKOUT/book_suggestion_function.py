import random

def get_suggestion(database):
    index = random.randint(0, 10)
    suggested_book = database[index]
    return suggested_book

def add_book(database, book):
    database.append(book)
    return database

def remove_book(database, book):
    database.remove(book)
    return database

def update_book(database, old_book, new_book):
    database.remove(old_book)
    database.append(new_book)
    return database

def show_all_book(database):
    return database
