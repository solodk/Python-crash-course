# Start with your program from Exercise 9-1. Add an attribute called
# number_served with a default value of 0. Create an instance called
# restaurant from this class. Print the number of customers the restaurant
# has served, and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number of
# customers that have been served. Call this method with a new number and
# print the value again.
# Add a method called increment_number_served() that lets you increment the
# number of customers who've been served. Call this method with any number
# you like that could represent how many customers were served in, say, a day
# of business

class Restaurant:
    """Simple imitation of restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine_type =  cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f'{self.name} has a {self.cuisine_type} cuisine type')
    
    def open_restaurant(self):
        print(f'Restaurant is open now')
    
    def set_number_served(self, number):
        if number > self.number_served:
            self.number_served = number
        else:
            print('You can\'t set lower number')
    
    def increment_number_served(self, number):
        if number > 0:
            self.number_served += number
        else:
            print('You can\'t decreese the number')

restaurant = Restaurant('Puzata hata', 'Ukrainian')
print(restaurant.number_served)
#restaurant.number_served = 3563
#restaurant.set_number_served(223)
restaurant.increment_number_served(3333)
print(restaurant.number_served)

