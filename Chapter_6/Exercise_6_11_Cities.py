# Make a dictionary called cities. 
# Use the names of three cities as keys in your dictionary. 
# Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. 
# The keys for each city’s dictionary should be something like country, population, and fact. 
# Print the name of each city and all of the information you have stored about it.

cities = {
    'Kyiv':{
        'country':'Ukraine',
        'population':'3m',
        'fact':'The most visited McDonald\'s',
    },
    'London':{
        'country':'Great Britain',
        'population':'9,6m',
        'fact':'Police never caught Jack the Ripper',
    },
    'Lisbon':{
        'country':'Portugal',
        'population':'3m', 
        'fact':'Lisbon is one of the oldest cities of Europe',
    },
}

for city in cities:
    print(city.title())
    for k, v in cities[city].items():
        print(f'\t-{k.title()}: {v.title()}')