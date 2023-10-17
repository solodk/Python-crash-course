# Make a list or tuple containing a series of 10 numbers and 5 letters.
# Randomly sellect 4 numbers or letters from the list and print a message 
# saying that any ticket matching these 4 number or letters wins a prize.
from random import choice

some_list = [1, 'a', 3, 'g', 5, 'f', 2, 6, 'e', 'r']
winning_seq = [str(choice(some_list)) for i in range(4)]
winning_seq = ''.join(winning_seq).upper()
print(f'Any ticket matching {winning_seq} wins a prize')