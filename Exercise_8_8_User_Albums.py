# Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album's artist and titlle.
# Once you have that information, call make_album() with the 
# user's input and print the dictionary that's created. Be sure
# to include a quit value in the while loop. 

import Exercise_8_7_Album as ext
make_album = ext.make_album

print("Enter 'q' to quit")
while True:
    name = input("Artist name: ")
    if name == 'q':
        break
    album = input("Album name: ")
    if album == 'q':
        break
    print(make_album(name, album))
    
