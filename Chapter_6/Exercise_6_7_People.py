# Start with the program you wrote for Exercise 6-1. Make
# two new dictionaries representing different people, and store all three dictionar-
# ies in a list called people. Loop through your list of people. As you loop through
# the list, print everything you know about each person.

import Exercise_6_1_Person as ext

sanya = ext.person_info

oleg = {}
oleg['first_name'] = 'Oleg'
oleg['last_name'] = 'Tkachishyn'
oleg['age'] = 24
oleg['city'] = 'Kyiv'

katya = {}
katya['first_name'] = 'Katerina'
katya['last_name'] = 'Bezsmola'
katya['age'] = 27
katya['city'] = 'Kyiv'

people = [sanya, oleg, katya]

for person in people:
    print(f"{person['first_name'].title()} {person['last_name'].title()}")
    print(f"\tAge: {person['age']}")
    print(f"\tLives in: {person['city']}\n")