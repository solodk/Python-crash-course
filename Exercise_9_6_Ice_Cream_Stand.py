# An ice cream stand is a specific kind of restaurant. Write a class called
# IceCreamStand that inherits from the Restaurant class you wrote in Exercise
# 9-4. Either version of the class will work; just pick the one you like better
# Add an attribute called flavors that stores a list of ice cream flavors.
# Write a method that displays these flavors.
# Create an instance of IceCreamStand, and call this method.

from Exercise_9_4_Number_Served import Restaurant
print("#"*80)

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['chocolate', 'strawberry', 'kiwi']

    def display_flavors(self):
        print('We have flavors such as:')
        for flavor in self.flavors:
            print(f' - {flavor.title()}')

some_stand = IceCreamStand('MyOwnStand', 'ice cream')
some_stand.display_flavors()