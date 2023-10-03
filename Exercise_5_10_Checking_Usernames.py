# Do the following to create a program that simulates how websites ensure that everyone has a unique username.
# 1) Make a list of five or more usernames called current_users.
# 2) Make another list of five usernames called new_users. Make sure one or
# two of the new usernames are also in the current users list. 
# 3) Loop through the new_users list to see if each new username has already
# been used. If it has, print a message that the person will need to enter a
# new username. If a username has not been used, print a message saying
# that the username is available.
# 4) Make sure your comparison is case insensitive. If 'John' has been used,
# 'JOHN' should not be accepted. (To do this, you'll need to make a copy of 
# current_users containing the lowercase versions of all existing users).

current_users = ['admin', 'test', 'John', 'Mary', 'Nick']
new_users = ['Oleg', 'john', 'supakilla']
copy_current_users = [username.lower() for username in current_users]

for new_user in new_users:
    if new_user.lower() in copy_current_users:
        print(f'Name {new_user} already exists')
    else:
        print(f'{new_user} in available')