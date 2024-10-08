class MissingKeywordError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self, message)
from functions import *

input_file = ''
output_file = ''
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
            # Removes the whitespace
            remove_whitespace(input_file, output_file)
        if option == 2:
            # Checks for keywords, identifiers, operators, delimiters, and literals and adds them to a dictionary
            check_keywords(reserved_keywords)
            check_identifiers(reserved_identifiers)
            check_operators(reserved_operators)
            check_delimiters(reserved_delimiters)
            check_litterals(reserved_litterals)
        if option == 3:
            # Shows the table
            pass
        if option == 4:
            # Clears the tables
            pass
        if option == 5:
            print('\nThank you for using the Program! Created by Inigo Zulueta')
            break
    except ValueError:
        print("\nInvalid attempt. Please try again.")