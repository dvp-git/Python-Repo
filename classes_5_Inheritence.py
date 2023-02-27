# Demo of Inheritance

#class ChildClass(BaseClass):

class Aircraft:

    def num_seats(self):
        row, row_seats = self.seating_plan()
        return len(row) * len(row_seats)

class AirbusA319(Aircraft):

    def __init__(self, registration):
        self._registration = registration

    def get_registration(self):
        return self._registration

    def get_model(self):
        return "Airbus A319"

    def seating_plan(self):
        return range(1,23),"ABCDEF"

class Boeing777(Aircraft):

    def __init__(self, registration):
        self._registration = registration

    def get_registration(self):
        return self._registration

    def get_model(self):
        return "Boeing 777"

    def seating_plan(self):
        return range(1,56),"ABCDEFGHJK"



a = AirbusA319("G-EZBT")
print(a.num_seats())

b = Boeing777("N717AN")
print(b.num_seats())
