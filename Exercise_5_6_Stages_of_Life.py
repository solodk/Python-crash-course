# Write an if-elif-else chain that determines a person's stage of life.
# Set a value for the variable age, and then:
# 1) If the person is less than 2 years old, print a message that the person is a baby. 
# 2) If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
# 3) If the person is at least 4 years old but less than 13, print a message that the person is a kid. 
# 4) If the person is at least 13 years old but less than 20, print a message that the person is a teenager. 
# 5) If the person is at least 20 years old but less than 65, print a message that the person is an adult.
# 6) If the person is age 65 or older, print a message that the person is an elder.
7
age = int(input('Enter your age: '))

if age < 0:
    print('Wrong number')
elif age < 2:
    print('You are a baby')
elif age < 4:
    print('You are a toddler')
elif age < 13:
    print('You are a kid')
elif age < 20:
    print('You are a teenager')
elif age < 65:
    print('You are an adult')
else:
    print('You are an elder')