# Write a separate Privileges class. The class should have one attribute,
# privileges, that stores a list of string as described in Exercise 9-7
# Move the show privileges method to this class. Make a Privileges instance
# as an attribute in the Admin class. Create a new instance of Admin and use
# your method to show its privileges.

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f'{self.first_name.title()} {self.last_name.title()}')

    def greet_user(self):
        print(f'Greetings {self.first_name.title()}!\n')
    
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Privileges():
    def __init__(self, privileges):
        self.privileges = privileges

    def show_previleges(self):
        print("Admin can:")
        for previlege in self.privileges:
            print(f" - {previlege}")

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges(
            ["can add post", "can delete post", "can ban user"]
            )

some_admin = Admin("Nick", "Sweet")
some_admin.privileges.show_previleges()