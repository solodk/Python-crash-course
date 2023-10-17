# Modify your program from Exercise 6-2 so each person can have more than one favorite number. 
# Then print each person’s name along with their favorite numbers.

favourite_numbers = {}

favourite_numbers['Sasha'] = 55, 11
favourite_numbers['Vitalik'] = 93, 53
favourite_numbers['Bogdan'] = 45, 4
favourite_numbers['Nick'] = 3, 5
favourite_numbers['Olena'] = 1, 22

for name, numbers in favourite_numbers.items():
    print(f"{name.title()}'s favourite number is: ")
    for number in numbers:
        print(f' {number}')
