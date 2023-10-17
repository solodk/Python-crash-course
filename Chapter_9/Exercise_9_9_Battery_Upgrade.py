# Use the final version of electric_car.py from this section. Add a method to
# the Battery class called upgrade_battery(). This method should check the
# battery size and set the capacity to 65 if it isn't already. Make an
# electric car with a default battery size, call get_range() once, and then
# call get_range() a second time after upgrading the buttery. You should see
# an increase in the car's range.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = f"{make} {model} {year}"
        return long_name.title()
    
    def read_odometer(self):
        print(f'This car has {self.odometer_reading} miles on it')

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = number
        else:
            print('You can\'t roll back an odometer!')
    
    def increment_odometer(self, miles):
        if miles > 0:
            self.odometer_reading += miles
        else:
            print('You can\'t roll back an odometer!')

class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery")

    def upgrade_battery(self):
        self.describe_battery()
        if self.battery_size < 65:
            self.battery_size = 65
    
    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")


class ElecticCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

some_car = ElecticCar('nissan', 'leaf', 2024)
some_car.battery.get_range()
some_car.battery.upgrade_battery()
some_car.battery.get_range()