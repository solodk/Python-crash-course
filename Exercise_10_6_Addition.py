# One common problem when prompting for numberical input occurs when people
# provide text instead of numbers. When you try to convert the input to an int,
# you'll get a ValueError. Write a program that prompts for two numbers. Add
# them together and print the result. Catch the ValueError if either input
# value is not a number, and print a friendly error message. Test your program
# by entering two numbers and then by entering some text instead of a number

try:
    number1 = int(input("Enter a first number: "))
    number2 = int(input("Enter a second number: "))
except ValueError:
    print('Sorry, this is not a number')

print(number1+number2)