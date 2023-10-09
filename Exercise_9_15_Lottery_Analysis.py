# You can use a loop to see how hard it might be to win the kind of lottery
# you just modeled. Make a list or tuple called my_ticket. Write a loop that
# keeps pulling numbers until your ticket wins. Print a message reporting
# how many times the loop had to run to give you a winning ticket.

from random import choice
some_list = [1, 'a', 3, 'g', 5, 'f', 2, 6, 'e', 'r']

my_ticket = ' '
winning_seq = ''
counter = 0

while my_ticket != winning_seq:
    counter += 1
    winning_seq = [str(choice(some_list)) for i in range(4)]
    winning_seq = ''.join(winning_seq).upper()
    my_ticket = [str(choice(some_list)) for i in range(4)]
    my_ticket = ''.join(my_ticket).upper()

print('Finaly I won.')
print(f' - My ticket: {my_ticket}')
print(f' - Winning sequence: {winning_seq}')
print(f' - Counter: {counter}')