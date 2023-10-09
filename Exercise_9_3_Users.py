# Make a class called User. Create two attributes called first_name and
# last_name, and then create several other attributes that are typically
# stored in a user profile. Make a method called describe_user() that prints
# a summary of the user's information. Make another method called greet_user()
# that prints a personalized greeting to the user.
# Create several instances representing different users, and call both methods
# for each user.

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f'{self.first_name.title()} {self.last_name.title()}')

    def greet_user(self):
        print(f'Greetings {self.first_name.title()}!\n')

user1 = User("Nick", "Sweet")
user2 = User('Mykola', 'Solodkyi')
user3 = User('Bambuk', 'Panama')

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()