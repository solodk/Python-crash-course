# Write a function that stores information about a car in a
# dictionary. The function should always recieve a manufacturer
# and a model name. It should then accept an arbitrary number of
# keyword arguments. Call the function with the required information
# and two other name-value pairs, such as a color or an optional
# feature. Your function should work for a call like this one:
#   car = make_car('subaru', 'outback', color='blue', tow_package=True)
# Print the dictionary that's returned to make sure all the information
# was stored correctly

def make_car(brand, car_type, **car_info):
    car_info['brand'] = brand
    car_info['type'] = car_type
    return car_info


car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)