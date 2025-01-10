"""
CS1026a 2023
Assignment 02
Matt Farzaneh
251370889
mfarzan
Date Completed: October, 10, 2023

This program creates a system where you can add and borrow books
while it keeps track of the borrowing history
"""


# start function
def start():
    # program continues until exited using the exit function
    go = True
    # initial book list
    all_books = [
        ['9780596007126', "The Earth Inside Out", "Mike B", 2, ['Ali']],
        ['9780134494166', "The Human Body", "Dave R", 1, []],
        ['9780321125217', "Human on Earth", "Jordan P", 1, ['David', 'b1', 'user123']]
    ]
    borrowed = []
    # start of loop
    while go:
        # calls menu print function after each action
        print_menu()
        user_input = input('Your selection> ')
        # calls add book function
        if user_input.lower() == 'a' or user_input == '1':
            all_books = all_books_app(all_books, add(all_books, borrowed))
        # calls borrowed book function
        elif user_input.lower() == 'r' or user_input == '2':
            all_books, borrowed = borrow(all_books, borrowed)
        # calls return book function
        elif user_input.lower() == 't' or user_input == '3':
            all_books, borrowed = return_books(all_books, borrowed)
        # calls list books function
        elif user_input.lower() == 'l' or user_input == '4':
            list_books(all_books, borrowed)
        # exits the program
        elif user_input.lower() == 'x' or user_input == '5':
            exit_pro(all_books, borrowed)
        # error message for unexpected input
        else:
            print('Wrong selection! Please select a valid option')


# adds book to allBooks list
def all_books_app(allBooks, book):
    allBooks.append(book)
    return allBooks


# exit function
def exit_pro(all_books, borrowed):
    print("\n$$$$$$$$ FINAL LIST OF BOOKS $$$$$$$$")
    list_books(all_books, borrowed)
    exit()


# prints the menu
def print_menu():
    print('\n#######################')
    print('1: (A)dd a new book.')
    print('2: Bo(r)row books.')
    print('3: Re(t)urn a book.')
    print('4: (L)ist all books.')
    print('5: E(x)it.')
    print('#######################\n')


# add function
def add(allBooks, borrowed):
    # sets all inputs to be invalid
    # only continues when they become true
    valid_input = False
    valid_input2 = False
    valid_input3 = False
    # makes sure expected input is made and stored
    # asks again if unexpected input
    while not valid_input:
        # asks for name of book
        bookName = input('Book name> ')
        # error testing
        if '*' in bookName or '%' in bookName:
            print('Invalid book name!')
        # if valid input continue
        else:
            valid_input = True

    # asks and stores author name
    author = input('Author name> ')

    # asks and stores book edition
    while not valid_input2:
        edition = input('Edition> ')
        # error testing
        # makes sure value is an integer
        if not edition.isdigit():
            print('Enter a valid number')
        # continues of valid input
        else:
            edition = int(edition)
            valid_input2 = True

    # asks for ISBN
    while not valid_input3:
        isbn = input('ISBN> ')
        # if input not an integer invalid input
        if isbn.lower() == 'x' or isbn == '5':
            exit_pro(allBooks, borrowed)
        elif not isbn.isdigit():
            print('Invalid ISBN')
        # if length not 13 invalid input
        elif len(isbn) != 13:
            print('Invalid ISBN')
        else:
            sum_n = 0
            for i in range(13):
                # multiplies even digit position by 1
                if i % 2 == 0:
                    sum_n = sum_n + int(isbn[i]) * 1
                # multiplies odd digit position by 3
                else:
                    sum_n = sum_n + int(isbn[i]) * 3
            # if the sum of all numbers x check code not a multiple of 10 = error
            if sum_n % 10 != 0:
                print("Invalid ISBN")
            # store ISBN and continue
            else:
                isbn = int(isbn)
                valid_input3 = True
    # stores book info inside of list
    oneNewBook = [isbn, bookName, author, edition, []]
    print("A new book is added successfully")
    # return book info
    return oneNewBook


# borrow method
def borrow(allBooks, borrowed):
    exists = False
    # create name list and borrowed list
    name_list = []
    borrowed = []
    # stores borrower name
    name = input("Enter the borrower name> ")
    # search through the all books list name list
    search = input("Search term> ")
    # if search ends with *
    if search.endswith("*"):
        # get rid of last term (*)
        search = search[:-1]
        # traverses through 2D list (allBooks)
        for i in range(len(allBooks)):
            # if the inputted search is found in allBooks
            if search in allBooks[i][1]:
                print("---------------")
                print("[Available]")
                print(allBooks[i][1] + " - " + allBooks[i][2])
                print("E: " + str(allBooks[i][3]) + " ISBN: " + str(allBooks[i][0]))
                print("borrowed by:", name_list)
                exists = True
                # add name connected to specific book in allBooks list
                allBooks[i][4].append(name)
                # add book list to borrowed list
                borrowed.append(allBooks[i])
                # remove book list from allBooks list
                allBooks.remove(allBooks[i])
                # exits function
                return allBooks, borrowed

    # if search ends with %
    elif search.endswith("%"):
        # remove ending term
        search = search[:-1]
        # traverses through all books 2D list
        for i in range(len(allBooks)):
            # if book found
            if allBooks[i][1].startswith(search):
                print("---------------")
                print("[Available]")
                print(allBooks[i][1] + " - " + allBooks[i][2])
                print("E: " + str(allBooks[i][3]) + " ISBN: " + str(allBooks[i][0]))
                print("borrowed by:", name_list)
                exists = True
                # add name connected to specific book in allBooks list
                allBooks[i][4].append(name)
                # add book list to borrowed list
                borrowed.append(allBooks[i])
                # remove book list from allBooks list
                allBooks.remove(allBooks[i])
                # exits function

    else:
        # traverses through 2D list
        for i in range(len(allBooks)):
            # if search is exactly the book name
            if search == allBooks[i][1]:
                print("---------------")
                print("[Available]")
                print(allBooks[i][1] + " - " + allBooks[i][2])
                print("E: " + str(allBooks[i][3]) + " ISBN: " + str(allBooks[i][0]))
                print("borrowed by:", name_list)
                exists = True
                # add name connected to specific book in allBooks list
                allBooks[i][4].append(name)
                # add book list to borrowed list
                borrowed.append(allBooks[i])
                # remove book list from allBooks list
                allBooks.remove(allBooks[i])
                # exits function
                return allBooks, borrowed
        # if book not found
        if not exists:
            print("No books found!")
        # exits function
        return allBooks, borrowed


# return book function
def return_books(allBooks, borrowed):
    check = False
    # input the ISBN of the book you want to return
    try:
        isbn_ret = int(input("ISBN> "))
    # exits program if non integer value is inputted
    except ValueError:
        print("No book is found!")
        return allBooks, borrowed
    # traverses borrowed list
    for book in borrowed:
        # if ISBN found
        if isbn_ret == int(book[0]):
            # add book to allBooks list
            allBooks.append(book)
            # removes book from allBooks list
            borrowed.remove(book)
            check = True
            print("Book returned successfully!")
            # exits function
            return allBooks, borrowed
    # if book not found
    if not check:
        print("No book is found!")
    # exit function
    return allBooks, borrowed


# list book function
def list_books(allBooks, borrowed):
    # if book in allBooks list
    for book in allBooks:
        # print book list
        print("---------------")
        print("[Available]")
        print(book[1] + " - " + str(book[2]))
        print("E: " + str(book[3]) + " ISBN: " + str(book[0]))
        print("Borrowed by:", book[4])

    # if book in borrowed list
    for book in borrowed:
        # print borrowed list
        print("---------------")
        print("[Unavailable]")
        print(book[1] + " - " + str(book[2]))
        print("E: " + str(book[3]) + " ISBN: " + str(book[0]))
        print("Borrowed by:", book[4])


# start function
start()
