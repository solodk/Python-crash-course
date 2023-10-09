# Make a class called Restaurant. The __init__() method for Restaurant should
# store two attributes: a restaurant_name and a cuisine_type. Make a method
# called describe_restaurant() that prints these two pieces of information,
# and a method called open_restaurant() that prints a message indicating that
# the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes
# individually, and then call both methods.

class Restaurant:
    """Simple imitation of restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine_type =  cuisine_type

    def describe_restaurant(self):
        print(f'{self.name} has a {self.cuisine_type} cuisine type')
    
    def open_restaurant(self):
        print(f'Restaurant is open now')

some_restaurant = Restaurant('Puzata hata', 'Ukrainian')
print(f"restaurant name: {some_restaurant.name}")
print(f"cuisine type: {some_restaurant.cuisine_type}")
some_restaurant.describe_restaurant()
some_restaurant.open_restaurant()