# Closing with Context managers

# The with statement construct works with any object that follows the context-manager protocols
from contextlib import closing
""" Demonstrating raid on a Refridgerator"""

class RaidRefridgerator:
    ''' Raid a Refridgerator'''

    def open(self):
        print(" Open the fridge door")


    def take_food(self, food):
        print("Finding the item {}".format(food))
        if food == "deep fried pizza":
            raise RuntimeError("Health warning!")
        print("Taking {} ". format(food))


    def close(self):
        print("Close the fridge door")


def raid(food):
    with closing(RaidRefridgerator()) as r:
    # r = RaidRefridgerator()
        r.open()
        r.take_food(food)
        # r.close()

raid('deep fried pizza')   ## Here we are interrupted by RuntimeError and din't close the door
