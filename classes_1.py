# Classes

"""Model for an aircraft """

class Flight:
    pass

    def __init__(self,number):
        self.number = number

    def number(self):
        return self.number

f = Flight(10234)


print(f.number)
