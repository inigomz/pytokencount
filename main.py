class MissingKeywordError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self, message)
from functions import *


def menu_generator():
    '''
    Infinite generator used for the menu.
    The reason why I would use a generator over something else is because I didn't want this to get stored in memory, just in case a user
    has a relatively large contact list for whatever reason.
    '''
    yield "1. Remove Whitespaces"
    yield "2. Count all tokens"
    yield "3. Show a Lexeme and Token Table"
    yield "4. Clear tokens"
    yield "5. Exit the program"

while True:
    menu = menu_generator()

    print("*** PYTHON TOKEN/LEXEME COUNTER MAIN MENU ***")
    for item in menu:
        print(item)
    option = int(input("Enter menu choice: "))
    try:
        if option == 1:
            remove_whitespace()
        if option == 2:
            modify_contact(contacts, id, first_name, last_name)
        if option == 3:
            delete_contact(id, contacts)
        if option == 4:
            sort_contacts(contacts)
        if option == 5:
            find_contact(contacts)
        if option == 6:
            print("\nThank you for using the program!")
            break
    except ValueError:
        print("\nInvalid attempt. Please try again.")