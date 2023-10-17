# Modify your except block in Exercise 10-7 to fail silently if either file is
# missing

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
    pass
