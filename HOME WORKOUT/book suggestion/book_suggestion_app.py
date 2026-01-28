from book_suggestion_function import get_suggestion, remove_book, add_book, update_book, show_all_books

def main_menu(my_list):
    menu = ("""
    WELCOME TO THE BOOK SUGGESTION SYSTEM!
    1. Get Suggestions
    2. Add Book
    3. Remove Book
    4. Update Book
    5. Show Books
    """)
    print(menu)
    option = input("Enter any Option From The Above 1 - 5 ")

    match(option):
        case "1":
                print("Book For the Day")
                print("Book Title:", get_suggestion)
                print("Page: ", page + 1)

        case "2":
                add = input("Enter The Book Title: ")
                add_book(my_list, book)               
                print("Book Added Successfully!")

        case "3":
                remove = input("Enter The Book Title To Remove: ")
                remove_book(my_list, book)
                print("Book Removed Successfully!")

        case "4":
                old_book = input("Enter The Old Book Title: ")
                new_book = input("Enter The New Book Title: ")
                update_book(my_list, old_book, new_book)
                print("Book Updated Successfully!")

        case "5":
                print("Your Book Collection: ", show_all_books)
                
                
                

def main():
    my_list = ["Odili in the Mystery of Speed", " the myth", "Raone" ]
    main_menu(my_list)

main()




    
