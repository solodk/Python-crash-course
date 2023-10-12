# You can use the replace() method to replace any word in a string with a
# different word.
# Read in each line from the file you just created, learning_python.txt, and
# replace the word Python with the name of another language, such as C. Print
# each modified line to the screen.

from pathlib import Path

file = Path('learning_python.txt')
content = file.read_text().replace('Python', 'C')

print(content)