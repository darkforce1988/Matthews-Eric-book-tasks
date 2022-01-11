from random import randint


class Die:
    """Models a die"""
    def __init__(self, sides=6):
        """Initialize die attributes"""
        self.sides = sides

    def roll_die(self):
        """Print a random number between 1 and the number of die sides"""
        print(randint(1, self.sides))


square_1 = Die()
for tries in range(10):
    square_1.roll_die()

square_2 = Die(10)
for tries in range(10):
    square_2.roll_die()

square_3 = Die(20)
for tries in range(10):
    square_3.roll_die()
