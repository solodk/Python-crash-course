# Write a program that prompts for the user's favorite number. Use json.dumps()
# to store this number in a file. Write a separate program that reads in this
# value and prints the message "I know your favorite number! It's ___"

from pathlib import Path
import json

favorite_number = int(input("Enter your favorite number: "))
file = Path("favorite_number.json")
content = json.dumps(favorite_number)

file.write_text(content)