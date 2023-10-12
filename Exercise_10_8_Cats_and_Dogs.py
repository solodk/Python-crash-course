# Make two files, cats.txt and dogs.txt. Store at least three names of cats in
# the first file and three name of dogs in the second file. Write a program
# that tries to read these files and print the content of the file to the 
# screen. Wrap your code in a try-except block to catch the FileNotFound error,
# and print a friendly message if a file is missing. Move one of the files to 
# a different location on your system, and make sure the code in the except
# block executes properly.

from pathlib import Path

try:
    cats = Path('cats.txt')
    dogs = Path('dogs.txt')
    cat_names = cats.read_text()
    dog_names = dogs.read_text()
    
    print('Cat names:')
    for name in cat_names.splitlines():
        print(f" - {name.title()}")

    print('Dog names:')
    for name in dog_names.splitlines():
        print(f" - {name.title()}")

except FileNotFoundError:
    print('Sorry, file not found')
