def main_menu(database):
    prompt = """
        1 Get Suggestions
        2. Add Book
        3. Remove Book
        4. Update Book
        5. Show all Books

            """
    print(prompt)
    option = input("Enter any option from 1 -5 : ")

    match(option):
            case "1": print("Enter a book title ")
                      print("Pages", )


def main():
    database = ["Reason For Speed", "The Forces Of Evil", "Odili The Best", "Semicolon"]
    main_menu()
    pass

main()

