# Make a dictionary called favorite_places. 
# Think of three names to use as keys in the dictionary, and store to these favorite places for each person. 
# To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. 
# Loop through the dictionary, and print each person's name and their favorite places. 

favorite_places = {
    'eric': ['bear mountain', 'death valley', 'tierra del fuego'],
    'erin': ['hawaii', 'iceland'],
    'ever': ['mt. verstovia', 'the playground', 'south carolina']
    }

for name, places in favorite_places.items():
    print(f"\n {name.title()} likes the following places:")
    for place in places:
        print(f"- {place.title()}")