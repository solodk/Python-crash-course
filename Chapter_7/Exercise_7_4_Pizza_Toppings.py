# Write a loop that prompts the user to enter a series of 
# pizza toppings until they enter a 'quit' value. As they enter each topping, print
# a message saying you'll add that topping to their pizza

while True:
    message = 'Enter a pizza topping'
    message += '\nEnter "quit" to exit '
    pizza_topping = input(message)

    if pizza_topping == 'quit':
        break
    else:
        print(f'\nAdded a {pizza_topping}\n')