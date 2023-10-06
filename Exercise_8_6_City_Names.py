# Write a function called city_country() that takes in the name
# of a city and its country. The function should return a string
# formatted like this: "Santiago, Chile"
# Call your function with at least three city-country pairs, and
# print the values that are returned.

def city_country(city, country):
    """Returns string like 'Santiago, Chile'"""
    message = f"{city.title()}, {country.title()}"
    return message

print(city_country('kyiv', 'ukraine'))
print(city_country('lisbon', 'portugal'))
print(city_country('paris', 'france'))