# Start with your work from Exercise 9-8. Store the classes User, Privileges,
# and Admin in one module. Create a separate file, make an Admin instance, and
# call show_privileges() to show that everything is working correctly.

import users

admin = users.Admin('Nick', 'Sweet')
admin.privileges.show_privileges()