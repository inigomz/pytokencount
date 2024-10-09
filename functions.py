# Keeping this in here in the event I want to call upon different files other than input_file.txt or output_file.txt.
# Technically this MissingKeywordError will not be used.
class MissingKeywordError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self, message)

# TODO: Hey big head, don't forget to use this variable.
enable_docstring = False

def remove_whitespace(input_file, output_file):
    # Read the input file. In this case, it's a text file.
    with open(input_file, 'r') as f:
        # Side comment: If i need to read lines for a large database or smth, it's best that I create a hint parameter
        # just so I can avoid crashing my pc. Thank you for not making this overkill.
        lines = f.readlines()

    # Empty set that will hold each line in the text file as an element of the set.
    processed_lines = []
    # Returns a copy of a string with whitespaces and comments removed.
    for line in lines:

        if '#' in line:
            line = line[:line.index('#')]
            line = line.strip()
        if line:

        # Remove any additional comments using strip(), then use some sort of separator (in this case it's split()) 
        # to split and discard the rest of the whitespaces. We re-add a space using the join() and append() function to
        # concacenate the substrings with extra spaces removed.

        # What we get is no more whitespace. Each line becomes an element of the processed lines set (Line 12).
        # We add a string containing "space" in order to recombine the rest of the substrings.
        
            spaces = line.split()
            line = ' '.join(spaces)
            processed_lines.append(line)

    # We then open a new file and make it writable. Since each element of the set is a line, we write each element to 
    # the new file and separate each element with a \n. This gives us a new text file with no whitespaces and we are
    # ready to start processing the lexemes and tokens.
    with open(output_file, 'w') as f:
        for line in processed_lines:
            f.write(line + '\n')
    print('Whitespaces have been removed from the text.')

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
        print('Keywords have been successfuly processed')
        return reserved_keywords
    
def check_identifiers(reserved_identifiers, output_file):
    with open(output_file, 'r') as f:
        processed_file = f.read() 
        for identifier in reserved_identifiers:
            if identifier in processed_file:
                reserved_identifiers[identifier] += 1
        print('Identifiers have successfully been processed')
        return reserved_identifiers
    
def check_operators(reserved_operators, output_file):
    with open(output_file, 'r') as f:
        processed_file = f.read() 
        for operator in reserved_operators:
            if operator in processed_file:
                reserved_operators[operator] += 1
        print('Operators have successfully been processed')
        return reserved_operators
    
def check_delimiters(reserved_delimiters, output_file):
    with open(output_file, 'r') as f:
        processed_file = f.read() 
        for delimiter in reserved_delimiters:
            if delimiter in processed_file:
                reserved_delimiters[delimiter] += 1
        print('Delimiters have successfully been processed')
        return reserved_delimiters
        
def check_litterals(reserved_litterals, output_file):
    with open(output_file, 'r') as f:
        processed_file = f.read() 
        for litteral in reserved_litterals:
            if litteral in processed_file:
                reserved_litterals[litteral] += 1
        print('Litterals have successfully been processed')
        return reserved_litterals

# This is what shows the table. Pretty self explanitory. Combine all dictionaries into one
# while making sure everything looks pretty.
def show_lexemes():
    all_lexemes = reserved_keywords | reserved_identifiers | reserved_delimiters | reserved_litterals | reserved_operators
    # Nobody has time for formatting and making things look pretty 
    # (and I dont wanna guestimate with f strings).

    #Sets the width
    width = 15
    
    # Print header
    print(f"{'Lexeme'.center(width)} | {'Count'.center(width)}")
    print('-' * (width * 2 + 3))
    
    # Print each lexeme and its count
    for lexeme, count in all_lexemes.items():
        print(f"{lexeme.center(width)} | {str(count).center(width)}")
    
    # Print the total sum of lexemes
    total_lexemes = sum(all_lexemes.values())
    print('-' * (width * 2 + 3))
    print(f"{'Total'.center(width)} | {str(total_lexemes).center(width)}")