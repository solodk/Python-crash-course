# Make a list called sandwich_orders and fill it with the names of various sandwiches.
# Then make an empty list called finished_sandwiches.
# Loop through the list of sandiwich orders and print a message for each of finished sendwiches.
# After all the sendwiches have been made, print a message listing each sandwich that was made.

sandwich_orders = ['Chicken Sandwich', 'Egg Sandwich', 'Seafood Sandwich', 'Roast Beef Sandwich']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"Doing a {current_sandwich}")
    finished_sandwiches.append(current_sandwich)
    print(f"{current_sandwich.title()} is done\n")

print("\nAll sandwiches was done")