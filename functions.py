# Keeping this in here in the event I want to call upon different files other than input_file.txt or output_file.txt.
# Technically this MissingKeywordError will not be used.
class MissingKeywordError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self, message)

def remove_whitespace(input_file, output_file):
    # Read the input file. In this case, it's a text file.
    with open(input_file, 'r') as f:
        # Side comment: If i need to read lines for a large database or smth, it's best that I create a hint parameter
        # just so I can avoid crashing my pc. Thank you for not making this overkill.
        lines = f.readlines()
    
    docstring_check = False

    # Empty set that will hold each line in the text file as an element of the set.
    processed_lines = []
    # Returns a copy of a string with whitespaces and comments removed.
    for line in lines:

        linecheck = line.strip()
        # Check to see if docstrings are included.
        if linecheck.startswith('"""'):
            docstring_check = not docstring_check
            continue
        
        if docstring_check:
            continue

        # Removes comments that contain '#'
        if '#' in line:
            line = line[:line.index('#')]
            line = line.strip()
        if line:

        # Remove any additional comments using strip(), then use some sort of separator (in this case it's split()) 
        # to split and discard the rest of the whitespaces. We re-add a space using the join() and append() function to
        # concacenate the substrings with extra spaces removed.

        # What we get is no more whitespace. Each line becomes an element of the processed lines set (Line 12).
        # We add a string containing "space" in order to recombine the rest of the substrings.
          
            line = ' '.join(line.split())
            processed_lines.append(line)
        if '' in processed_lines:
            processed_lines.remove('')


    # We then open a new file and make it writable. Since each element of the set is a line, we write each element to 
    # the new file and separate each element with a \n. This gives us a new text file with no whitespaces and we are
    # ready to start processing the lexemes and tokens.
    with open(output_file, 'w') as f:
        for line in processed_lines:
            f.write(line + '\n')
    print('\nWhitespaces have been removed from the text. \n\n')

# Create multiple dictionaries of keywords, identifiers, etc. Since this is a small project I can get away with only listing keywords used
# for the example code.
reserved_keywords = {
    'def' : 0,
    'if' : 0,
    'print' : 0,
    'return' : 0,
    'for' : 0,
    'in' : 0,
    'range' : 0
    }
reserved_identifiers = {
    'calculate_sum' : 0,
    'greet' : 0,
    'a' : 0,
    'b' : 0,
    '__name__' : 0,
    '__main__' : 0,
    'num1' : 0,
    'num2' : 0,
    'result' : 0,
    'count' : 0,
    'i' : 0,
    }
reserved_operators = {
    '=' : 0,
    '==' : 0,
    '+' : 0,
    }
reserved_delimiters = {
    '(' : 0,
    ')' : 0,
    ':' : 0,
    ',' : 0,
    '"' : 0,
    }
reserved_litterals = {
    '10' : 0,
    '20' : 0,
    'Hello, World!' : 0,
    '5' : 0,
    }

# Main idea behind the check functions is to make everything as reusable as possible.

# Pretty much: open file (hence process file) > check to see if token exists in the file using a dictionary >
# If token exists in the file, add 1 value to its key : value in the dictionary > return the dictionary.

# All of the check functions do the same thing with ONE exception: 
# They call upon different dictionaries with different key: value pairs.
def check_keywords(reserved_keywords, output_file):
    with open(output_file, 'r') as f:
        processed_file = f.read() 
        for keyword in reserved_keywords:
            if keyword in processed_file:
                reserved_keywords[keyword] += 1
        print('\n\nKeywords have been successfuly processed\n')
        return reserved_keywords
    
def check_identifiers(reserved_identifiers, output_file):
    with open(output_file, 'r') as f:
        processed_file = f.read() 
        for identifier in reserved_identifiers:
            if identifier in processed_file:
                reserved_identifiers[identifier] += 1
        print('Identifiers have successfully been processed\n')
        return reserved_identifiers
    
def check_operators(reserved_operators, output_file):
    with open(output_file, 'r') as f:
        processed_file = f.read() 
        for operator in reserved_operators:
            if operator in processed_file:
                reserved_operators[operator] += 1
        print('Operators have successfully been processed\n')
        return reserved_operators
    
def check_delimiters(reserved_delimiters, output_file):
    with open(output_file, 'r') as f:
        processed_file = f.read() 
        for delimiter in reserved_delimiters:
            if delimiter in processed_file:
                reserved_delimiters[delimiter] += 1
        print('Delimiters have successfully been processed\n')
        return reserved_delimiters
        
def check_litterals(reserved_litterals, output_file):
    with open(output_file, 'r') as f:
        processed_file = f.read() 
        for litteral in reserved_litterals:
            if litteral in processed_file:
                reserved_litterals[litteral] += 1
        print('Litterals have successfully been processed\n\n')
        return reserved_litterals

# This is what shows the table. Pretty self explanitory. Combine all dictionaries into one
# while making sure everything looks pretty.
def show_lexemes():

    # Unionize all the dictionaries together to create a dictionary full of lexemes.
    all_lexemes = reserved_keywords | reserved_identifiers | reserved_delimiters | reserved_litterals | reserved_operators
    
    # Nobody has time for formatting and making things look pretty 
    # (and I dont wanna guestimate with f strings).
    print('\n***PRINT OPTIONS***')
    print('\n1. Print all lexemes\n2. Print all keywords\n3. Print all identifiers\n4. Print all delimiters\n5. Print all litterals\n6. Print all operators.\n\nMenu Options (Type a number):')
    
    #Sets the width
    width = 15
    menu = 0
    
    menu = int(input('Please select a number: ' ))

    # 1. Print all tokens
    if menu == 1:
        # Print header for all categories
        print('\n')
        print(f"{'Lexeme'.center(width)} | {'Count'.center(width)}")
        print('-' * (width * 2 + 3))
    
        # Print each lexeme and its count
        for lexeme, count in all_lexemes.items():
            print(f"{lexeme.center(width)} | {str(count).center(width)}")
    
        # Print the total sum of lexemes
        total_lexemes = sum(all_lexemes.values())
        print('-' * (width * 2 + 3))
        print(f"{'Total'.center(width)} | {str(total_lexemes).center(width)}")
        print('\n')

    # 2. Print all reserved keywords
    if menu == 2:
        # Print header for reserved keywords
        print('\n')
        print(f"{'Reserved Keywords'.center(width)}")
        print(f"{'Lexeme'.center(width)} | {'Count'.center(width)}")
        print('-' * (width * 2 + 3))
    
        # Print each lexeme and its count
        for lexeme, count in reserved_keywords.items():
            print(f"{lexeme.center(width)} | {str(count).center(width)}")

        # Print the total sum of lexemes
        total_lexemes = sum(reserved_keywords.values())
        print('-' * (width * 2 + 3))
        print(f"{'Total'.center(width)} | {str(total_lexemes).center(width)}")
        print('\n')

    # 3. Print all reserved identifiers
    if menu == 3:
        # Print header for reserved identifiers
        print('\n')
        print(f"{'Reserved Identifiers'.center(width)}")
        print(f"{'Lexeme'.center(width)} | {'Count'.center(width)}")
        print('-' * (width * 2 + 3))
    
        # Print each lexeme and its count
        for lexeme, count in reserved_identifiers.items():
            print(f"{lexeme.center(width)} | {str(count).center(width)}")

        # Print the total sum of lexemes
        total_lexemes = sum(reserved_identifiers.values())
        print('-' * (width * 2 + 3))
        print(f"{'Total'.center(width)} | {str(total_lexemes).center(width)}")
        print('\n')
    
    # 4. print all reserved delimiters
    if menu == 4:
        # Print header for reserved keywords
        print('\n')
        print(f"{'Reserved Delimiters'.center(width)}")
        print(f"{'Lexeme'.center(width)} | {'Count'.center(width)}")
        print('-' * (width * 2 + 3))
    
        # Print each lexeme and its count
        for lexeme, count in reserved_delimiters.items():
            print(f"{lexeme.center(width)} | {str(count).center(width)}")

        # Print the total sum of lexemes
        total_lexemes = sum(reserved_delimiters.values())
        print('-' * (width * 2 + 3))
        print(f"{'Total'.center(width)} | {str(total_lexemes).center(width)}")
        print('\n')
    
    # 5. print all reserved litterals
    if menu == 5:
        # Print header for reserved keywords
        print('\n')
        print(f"{'Reserved litterals'.center(width)}")
        print(f"{'Lexeme'.center(width)} | {'Count'.center(width)}")
        print('-' * (width * 2 + 3))
    
        # Print each lexeme and its count
        for lexeme, count in reserved_litterals.items():
            print(f"{lexeme.center(width)} | {str(count).center(width)}")

        # Print the total sum of lexemes
        total_lexemes = sum(reserved_litterals.values())
        print('-' * (width * 2 + 3))
        print(f"{'Total'.center(width)} | {str(total_lexemes).center(width)}")
        print('\n')
    
    # 6. print all reserved operators
    if menu == 6:
        # Print header for reserved keywords
        print('\n')
        print(f"{'Reserved Operators'.center(width)}")
        print(f"{'Lexeme'.center(width)} | {'Count'.center(width)}")
        print('-' * (width * 2 + 3))
    
        # Print each lexeme and its count
        for lexeme, count in reserved_operators.items():
            print(f"{lexeme.center(width)} | {str(count).center(width)}")

        # Print the total sum of lexemes
        total_lexemes = sum(reserved_operators.values())
        print('-' * (width * 2 + 3))
        print(f"{'Total'.center(width)} | {str(total_lexemes).center(width)}")
        print('\n')

