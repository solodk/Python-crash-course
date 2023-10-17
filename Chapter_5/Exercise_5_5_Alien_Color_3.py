# Tunr your if-else chain from Exercise 5-4 into an if-elif-else chain.
# If the alien is green, print a message that the player earned 5 points.
# If the alien is yellow, print a message that the player earned 10 points.
# If the alien is red, print a message that the player earned 15 points.
# Write three versions of this program, making sure each message if printed for the appropriate color alien. 

def bang(alien):
    if alien == 'green':
        points = 5
    elif alien == 'yellow':
        points = 10
    elif alien == 'red':
        points = 15

    print(f'You just earned {points} points\n')

alien_color = 'red'
bang(alien_color)

alien_color = 'yellow'
bang(alien_color)

alien_color = 'green'
bang(alien_color)