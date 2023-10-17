# An administrator is a special kind of user. Write a class called Admin that
# inherits from the User class you wrote in Exercise 9-3 or 9-5. Add an
# attribute, privileges, that stores a list of strings like "can add post",
# "can delete post", "can ban user", and so on. Write a method called
# show_previleges() that lists the administrator's set of privileges. Create
# an instance of Admin, and call your method

from Exercise_9_5_Login_Attempts import User
print("#"*80)

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = ["can add post", "can delete post", "can ban user"]
    def show_previleges(self):
        print("Admin can:")
        for previlege in self.privileges:
            print(f" - {previlege}")

some_admin = Admin("Nick", "Sweet")
some_admin.show_previleges()