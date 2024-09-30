# Testing with dictionaries and key-value pairs
keyword_category = {
'def' : 0,
'if' : 0,
'print' : 0,
}

# Testing for incramentals
text_file = "def if print owl rain ( ) , : 2 1 3"
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
        else:
            return keyword_category
# main test program
#test_for_incramentals(keyword_category, text_file)
test_for_loop_incramentals(keyword_category, text_file)
print(keyword_category)