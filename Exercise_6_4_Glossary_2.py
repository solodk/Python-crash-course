# Now that you know how to loop through a dictionary, clean 
# up the code from Exercise 6-3 by replacing your series of print()
# calls with a loop that runs through the dictionary's keys and values. When
# you're sure that your loop works, add five more Python terms to your glossary.
# When you run your program again, these new words and meanings should 
# automatically be included in the output.

glossary = {}

glossary['is'] = 'The “is” keyword in Python is used to test object identity. That means Python simply compares the memory address a object resides in.'
glossary['or'] = 'The or keyword is a logical operator. The return value will be True if one of the statements return True, otherwise it will return False.'
glossary['as'] = 'Used to create an alias'
glossary['del'] = 'Used to delete an object'
glossary['with'] = 'Used to simplify exception handling'
glossary['raise'] = 'Used to raise an exception'
glossary['lambda'] = 'Used to create an anonymous function'

for key, value in glossary.items():
    print(f'{key}\n\t-{value}')