# Ask the user for a number, and then report whether the 
# number is multiple of 10 or not.

number = input('Enter a number: ')
number = int(number)

if number % 10 == 0:
    print("Your number is multiple of 10")
else:
    print("Your number is NOT multiple of 10")