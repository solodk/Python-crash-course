# Using one of the programs you wrote in this chapter,
# add several lines to the end of the program that do the following:
# 1) Print the message 'The first three items in the list are:'.
# Then use a slice to print the first three items from that program's list.
# 2) Print the message 'Three items from the middle of the list are:'
# Then use a slice to print three items from the middle of the list.
# 3) Print the message 'The last three items in the list are:'
# Then use a slice to print the last three items in the list.

import Exercise_4_8_Cubes as ext

seq = ext.cubes
middle = int(len(seq)/2)

print(f"The first three items in the list are: {seq[:3]}")
print(f"Three items from the middle of the list are: {seq[middle:middle+3]}")
print(f"The last three items in the list are: {seq[-3:]}")