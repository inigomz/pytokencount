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
    # Returns a copy of a string with whitespaces removed.
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

def check_keywords(output_file):
    
    # Create a dictionary of keywords. Since this is a small project I can get away with only listing keywords used
    # for the example code.
    reserved_keywords = {
        'def',
        'if',
        'print',
    }
    #TODO: Print the lexemes and count the number of keyword tokens.