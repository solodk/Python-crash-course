# The remember_me.py example only stores one piece of information, the
# username. Expand this example by asking for two more pieces of information
# about the user, then store all the information you collect in a dictionary.
# Write this dictionary to a file using json.dumps(), and read it back in
# using json.loads(). Print a summary showing exactly what your program
# remembers about user.

from pathlib import Path
import json

def greet_user():
    file = Path('username.json')
    user_info = get_dictionary(file)
    if user_info:
        print(f"Greetings, {user_info['username'].title()}!")
        print(f"I know your favorite number! It's {user_info['number']}")
        print(f"You will be 25 soon isn't?")
    else:
        prompt_user(user_info)
        write_dictionary(file, user_info)
    

def get_dictionary(path):
    try:
        content = path.read_text()
        dictionary = json.loads(content)
    except FileNotFoundError:
        dictionary = {}
    return dictionary

def write_dictionary(path, dictionary):
    content = json.dumps(dictionary)
    path.write_text(content)    

def prompt_user(dictionary):
    dictionary['username'] = input("What is your name? ")
    dictionary['age'] = input("How old are you? ")
    dictionary['number'] = input("What is your favorite number? ")
    return dictionary

greet_user()