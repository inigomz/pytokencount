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

# Create multiple dictionaries of keywords, identifiers, etc. Since this is a small project I can get away with only listing keywords used
# for the example code.
reserved_keywords = {
    'def' : 0,
    'if' : 0,
    'print' : 0,
    'return' : 0,
    }
reserved_identifiers = {
    'calculate_sum' : 0,
    'a' : 0,
    'b' : 0,
    '__name__' : 0,
    '__main__' : 0,
    'num1' : 0,
    'num2' : 0,
    'result' : 0,
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
    }

# Main idea behind the check functions is to make everything as reusable as possible.

# All of the check functions do the same thing with ONE exception: 
# They call upon different dictionaries with different key: value pairs.
def check_keywords(reserved_keywords, output_file):
    for keyword in reserved_keywords:
        if keyword in output_file:
            reserved_keywords[keyword] += 1
        else:
            print('Keywords have been successfuly processed')
            return reserved_keywords
    
def check_identifiers (reserved_identifiers, output_file):
    for identifier in reserved_identifiers:
        if identifier in output_file:
            reserved_identifiers[identifier] += 1
        else:
            print('Identifiers have successfully been processed')
            return reserved_identifiers
def check_operators (reserved_operators, output_file):
    for operator in reserved_operators:
        if operator in output_file:
            reserved_operators[operator] += 1
        else:
            print('Operators have successfully been processed')
            return reserved_operators
def check_delimiters (reserved_delimiters, output_file):
    for delimiter in reserved_delimiters:
        if delimiter in output_file:
            reserved_delimiters[delimiter] += 1
        else:
            print('Delimiters have successfully been processed')
            return reserved_delimiters
def check_litterals (reserved_litterals, output_file):
    for litteral in reserved_litterals:
        if litteral in output_file:
            reserved_litterals[litteral] += 1
        else:
            print('Litterals have successfully been processed')
            return reserved_litterals
    
    #TODO: Print the lexemes and count the number of keyword tokens.

def show_lexemes ():
    pass