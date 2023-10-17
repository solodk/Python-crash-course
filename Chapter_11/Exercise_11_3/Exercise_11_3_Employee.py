#   Write a class called Employee. The __init__() method should take iin a first
# name, a last name, and an annual salary, and store each of these as
# attributes. Write a method called give_rise() that adds $5,000 to the annual
# salary by default but also accepts a different rise amount.
#   Write a test file for Employee with two test functions, 
# test_give_default_rise() and test_give_custom_rise(). Write your tests once
# without using a fixture, and make sure they both pass. Then write a fixture
# so you don't have to create a new employee instance in each test function.
# Run the tests again, and make sure both tests still pass.

class Employee:
    def __init__(self, first, last, salary):
        self.first_name = first
        self.last_name = last
        self.salary = salary

    def give_rise(self, amount=5000):
        if amount > 0:
            self.salary += amount
        print(f"You receive a rise! Now you have a ${self.salary} salary")