# Make a class Die with one attribute called sides, which has a default value
# of 6. Write a method called roll_die() that prints a random number between
# 1 and the number of sides the die has. Make a 6-sided die and roll it 10
# times.
# Make a 10-sided die and a 20-sided die. Roll each die 10 times.
from random import randint

class Die:
    def __init__(self, sides):
        self.sides = sides
    
    def roll_die(self):
        print("Rolling a dice")
        print(f"Number {randint(1, self.sides)}")

six_sided = Die(6)
six_sided.roll_die()

ten_sided = Die(10)
ten_sided.roll_die()

twenty_sided = Die(20)
twenty_sided.roll_die()