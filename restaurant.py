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

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['chocolate', 'strawberry', 'kiwi']

    def display_flavors(self):
        print('We have flavors such as:')
        for flavor in self.flavors:
            print(f' - {flavor.title()}')