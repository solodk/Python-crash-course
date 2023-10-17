# Add an if test to hello_admin.py to make sure the list of users is not empty
# 1) If the list is empty, print the message We need to find some users!
# 2) Remove all of the usernames from your list, and make sure the correct message is printed.

user_list = []

if user_list:
    for user in user_list:
        if user == 'admin':
            print(f'Hello {user}, would you like to see a status report?\n')
        else:
            print(f'Hello {user}, long time no see\n')
else:
    print('We need to find some users!')
