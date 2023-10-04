# Make several dictionaries, where each dictionary represents a different pet. 
# In each dictionary, include the kind of animal and the owner's name. 
# Store these dictionaries in a list called pets. 
# Next, loop through your list and as you do, print everything you know about each pet. 

dog = {
    'kind':'dog',
    'owner':'Sasha'
}
cat = {
    'kind':'cat',
    'owner':'Olena'
}
snake = {
    'kind':'snake',
    'owner':'Vlad'
}

pets = [dog, cat, snake]

for pet in pets:
    print(f"It's a {pet['kind']} and it's owner is {pet['owner'].title()}")