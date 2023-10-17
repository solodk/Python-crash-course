# Start with your program from Excercise 4-1. 
# Make a copy of the list of pizzas, and call it friend_pizzas.
# Then, do the following:
# 1) Add a new pizza to the original list. 
# 2) Add a different pizza to the list friend_pizzas. 
# 3) Prove that you have two separate lists. 
# Print the message 'My friend`s favourite pizzas are: ',
# and then use a for loop to print the second list. 
# Make sure each new pizza is stored in the appropriate list.

import Exercise_4_1_Pizzas as ext

my_pizza = ext.pizzas
friend_pizzas = my_pizza[:]

my_pizza.append('margarita')
friend_pizzas.append('bbq')

print('My friend`s favourite pizzas are: ')
for pizza in friend_pizzas:
    print(pizza.title())