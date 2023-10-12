# Wrap your code from Exercise 10-5 in a while loop so the user can continue
# entering numbers, even if they make a mistake and enter text instead of a
# number.

while True:
    try:
        number1 = int(input("Enter a first number: "))
        number2 = int(input("Enter a second number: "))
    except ValueError:
        print('Sorry, this is not a number')
        continue

    print(f'Result is {number1+number2}')

