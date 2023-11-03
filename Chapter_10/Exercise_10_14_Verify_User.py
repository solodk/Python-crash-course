# The final listings for remember_me.py assumes either that the user has
# already entered their username or that the program is running for the first
# time. We should modify it in case the current user is not the person who last
# used the program.

from pathlib import Path
import json

def greet_user():
    file = Path('username.json')
    user_info = get_dictionary(file)
    
    if user_info:
        reset = input(f"Are you {user_info['username'].title()}? y/n ")
        if reset == 'n':
            get_new_user(file, user_info)
        else:
            print(f"Greetings, {user_info['username'].title()}!")
            print(f"I know your favorite number! It's {user_info['number']}")
            print(f"You will be 25 soon isn't?")
    else:
        get_new_user(file, user_info)
    

def get_dictionary(path):
    try:
        content = path.read_text()
        dictionary = json.loads(content)
    except FileNotFoundError:
        dictionary = {}
    return dictionary

def get_new_user(path, dictionary):
    prompt_user(dictionary)
    write_dictionary(path, dictionary)

def write_dictionary(path, dictionary):
    content = json.dumps(dictionary)
    path.write_text(content)    

def prompt_user(dictionary):
    dictionary['username'] = input("What is your name? ")
    dictionary['age'] = input("How old are you? ")
    dictionary['number'] = input("What is your favorite number? ")
    return dictionary

greet_user()