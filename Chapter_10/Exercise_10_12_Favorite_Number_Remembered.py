# Combine the two programs you wrote in Exercise 10-11 into one file. If the
# number is already stored, report the favorite number to the user. If not,
# prompt for the user's favorite number and store it in a file. Run the program
# twice to see that it works.

from pathlib import Path
import json

try:
    file = Path("favorite_number.json")
    content = file.read_text()
    content = json.loads(content)
    print(f"I know your favorite number! It's {content}")
except FileNotFoundError:
    favorite_number = int(input("Enter your favorite number: "))
    content = json.dumps(favorite_number)
    file.write_text(content)