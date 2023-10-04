# Make a dictionary containing three major rivers and the country 
# each river runs through. One key-value pair might be 'nile': 'egypt'. 
# 1) Use a loop to print a sentence about each river, such as 'The Nile runs through Egypt'. 
# 2) Use a loop to print the name of each river included in the dictionary.
# 3) Use a loop to print the name of each country incluede in the dictionary.

river_cross = {}

river_cross['Great Britain'] = 'Thames'
river_cross['Ukraine'] = 'Dnipro'
river_cross['Egypt'] = 'Nile'

for key, value in river_cross.items():
    print(f'The {value.title()} runs through {key.title()}')

print('\nRivers mentioned:')
for river in set(river_cross.values()):
    print(river.title())

print('\nCountries mentioned:')
for country in set(river_cross.keys()):
    print(country.title())