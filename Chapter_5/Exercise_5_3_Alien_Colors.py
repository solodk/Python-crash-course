# Imagine an alien was just shot down in a game. 
# Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
# 1) Write an if statement to test whether the alien's color is green. If it is, print a massage that the player just earned 5 points.
# 2) Write one version of this program that passes the if test and another that fails. (The version that fails will have no output)

def bang(alien):
    if alien == 'green':
        print("You've earned a 5 points!\n")

alien_color = 'green'
bang(alien_color)

alien_color = 'red'
bang(alien_color)
