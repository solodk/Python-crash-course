# Open a blank file in your text editor and write a few lines summarizing what
# you’ve learned about Python so far. Start each line with the phrase In Python
# you can… Save the file as learning_python.txt in the same directory as your 
# exercises fro mthis chapter. Write a program that reads the file and prints 
# what you wrote three times. Print the contents once by reading in the entire 
# file, once by looping over the file object, and once by storing the lines in 
# a list and then working with them outside the with block.

from pathlib import Path

file = Path('learning_python.txt')
content = file.read_text()

lines = content.splitlines()

for line in lines:
    print(line)
print('*'*80)
print(content)