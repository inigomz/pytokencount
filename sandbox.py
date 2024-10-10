# Testing with dictionaries and key-value pairs
keyword_category = {
'def' : 0,
'if' : 0,
'print' : 0,
}
reserved_keywords = {
    'def' : 0,
    'if' : 0,
    'print' : 0,
    'return' : 0,
    }
randomdict = {
'+' : 0,
'=' : 1,
',' : 2,
}
output_file = 'output_file.txt'
total = 0
input_file = 'input_file.txt'
# Testing for incramentals
text_file = "def if print owl rain ( ) , : 2 1 3"

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

def test_for_incramentals(keyword_category, text_file):
    if 'def' in text_file:
        keyword_category['def'] += 1
    if 'if' in text_file:
        keyword_category['if'] += 1
    if 'print' in text_file:
        keyword_category['print'] += 1
    return keyword_category

def test_for_loop_incramentals(keyword_category, text_file):
    for keyword in keyword_category:
        if keyword in text_file:
            keyword_category[keyword] += 1
            #print(keyword_category)
        else:
            return keyword_category
def combine_dicts(keyword_category, randomdict):
    return keyword_category | randomdict
def add_dict_values(keyword_category, randomdict):
    return sum(keyword_category.values())+ sum(randomdict.values())
    
def check_keywords(reserved_keywords, output_file):
    #TODO: find a way to initialize the output file so it sets each word as a string.
    with open(output_file, 'r') as f:
        processed_file = f.read() 
        for keyword in reserved_keywords:
            if keyword in processed_file:
                reserved_keywords[keyword] += 1
        print('Keywords have been successfuly processed')
        return reserved_keywords

alldicts = keyword_category | randomdict
# main test program
##test_for_incramentals(keyword_category, text_file)
##test_for_loop_incramentals(keyword_category, text_file)
##combine_dicts(keyword_category, randomdict)
##alldicts = keyword_category | randomdict
##print(alldicts)
##combine_dicts(keyword_category, randomdict)
##total = add_dict_values(keyword_category, randomdict)
##print(total)
##open_output_file(output_file)
##check_keywords(reserved_keywords, output_file)
##print(reserved_keywords)
remove_whitespace(input_file, output_file)