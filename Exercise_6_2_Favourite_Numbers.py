# Use a dictionary to store people's favourite numbers. 
# Think of five names, and use them as keys in  your dictionary. 
# Think of favourite number for each person, and store each as a value in your dictionary. 
# Print each person's name and their favourite number. 
# For even more fun, poll a few friends and get some actual data for your program. 

favourite_numbers = {}

favourite_numbers['Sasha'] = 5
favourite_numbers['Vitalik'] = 9
favourite_numbers['Bogdan'] = 4
favourite_numbers['Nick'] = 3
favourite_numbers['Olena'] = 1

for name in favourite_numbers:
    print(f"{name.title()}'s favourite number is {favourite_numbers[name]}")