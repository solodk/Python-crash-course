# A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let's call it a glossary.
# 1) Think of five programming words you've learned about in the previous
# chapters. Use these words as the keys in your glossary, and store their
# meanings as values.
# 2) Print each word and it's meaning as neatly formated output. You might
# print the word followed by a colon and then its meaning, or print the word
# on one line and then print its meaning indented on a second line. Use the
# newline character (\n) to insert a blank line between each word-meaning
# pair in your output.

glossary = {}

glossary['is'] = 'The “is” keyword in Python is used to test object identity. That means Python simply compares the memory address a object resides in.'
glossary['or'] = 'The or keyword is a logical operator. The return value will be True if one of the statements return True, otherwise it will return False.'
glossary['as'] = 'Used to create an alias'
glossary['del'] = 'Used to delete an object'
glossary['with'] = 'Used to simplify exception handling'

for keyword in glossary:
    print(f'{keyword}\n-{glossary[keyword]}')