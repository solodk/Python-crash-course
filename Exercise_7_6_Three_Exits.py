# Write different versions of either Exercise 7-4 or 7-5 that do 
# each of the following at least once: 
# 1) Use a conditional test in the while statement to stop the loop. 
# 2) Use an active variable to control how long the loop runs. 
# 3) Use a break statement to exit the loop when the user enters a 'quit' value.

print('Type \'quit\' to finish program')

pizza_topping = ""
while pizza_topping != 'quit':
    message = 'Enter a pizza topping '
    pizza_topping = input(message)

    if pizza_topping != 'quit':
        print(f'\nAdded a {pizza_topping}\n')

active = True
while active:
    message = 'Enter a pizza topping '
    pizza_topping = input(message)

    if pizza_topping == 'quit':
        active = False
    else:
        print(f'\nAdded a {pizza_topping}\n')

while True:
    message = 'Enter a pizza topping '
    pizza_topping = input(message)

    if pizza_topping == 'quit':
        break
    else:
        print(f'\nAdded a {pizza_topping}\n')