# A buffet-style restaurant offers only fave basic foods. 
# Think of five simple foods, and store them in a tuple. 
# 1) Use a for loop to print each food the restaurant offers.
# 2) Try to modify one of the items, and make sure that Python rejects the change.
# 3) The restaurant changes its menu, replacing two of the items with different foods.
# Add a line that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.

menu = ('falafel', 'carbonara', 'steak', 'sandwich', 'french fries')

for food in menu:
    print(food.title())

# menu[0] = 'pizza'

menu = ('pizza', 'carbonara', 'steak', 'hamburger', 'french fries')
print('\nNew menu:')
for food in menu:
    print(food.title())