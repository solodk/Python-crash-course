# Using the list sandwich_orders from Exercise 7-8, make sure 
# the sandwich 'pastrami' appears in the list at least three times.
# Add code near the beginning of your program to print a message saying 
# the deli has run out of pastrami, and then use a while loop to remove all 
# occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami
# sandwiches end up in finished_sandwiches.

sandwich_orders = ['Chicken Sandwich', 'pastrami', 'Egg Sandwich', 'Seafood Sandwich', 'pastrami', 'Roast Beef Sandwich', 'pastrami']
finished_sandwiches = []

print("The Deli has run out of pastrami")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"Doing a {current_sandwich}")
    finished_sandwiches.append(current_sandwich)
    print(f"{current_sandwich.title()} is done\n")

print("\nAll sandwiches was done")


if 'pastrami' in finished_sandwiches:
    print("There is a pastrami in finished sandwiches")