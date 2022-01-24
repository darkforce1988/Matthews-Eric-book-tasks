from random import randint


class Die:
    """Models a die"""
    def __init__(self, sides=6):
        """Initialize die attributes"""
        self.sides = sides

    def roll_die(self):
        """Return a random number between 1 and the number of die sides"""
        return randint(1, self.sides)


def make_die_throws(tries, sides=6):
    """Print a result of die throws with number of tries"""
    die = Die(sides)
    for try_ in range(1, tries + 1):
        print(f"Throw of a {sides}-sided die №{try_}: "
              f"{die.roll_die()}")
    print()


make_die_throws(10)

make_die_throws(10, 10)

make_die_throws(10, 20)
