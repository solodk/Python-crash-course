# Write a program that prompts the user for their name. When they respond,
# write their name to a file called guest.txt

from pathlib import Path

file = Path('guest.txt')
content = ''

print("Enter 'q' to exit.")
while True:
    name = input("Write your name: ")
    if name == 'q':
        break
    else:
        content += name + '\n'

file.write_text(content)