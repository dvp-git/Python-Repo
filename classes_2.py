### Class initializers best practise

class Flight:
    """ Model for a Flight"""
    def __init__(self,number):
        if not number[:2].isalpha():
            raise ValueError("No airplane code in {}".format(number))

        if not number[:2].isupper():
            raise ValueError("Invalid Airline code in {}".format(number))

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError("Invalid Route code in {}".format(number))

        self._number = number

    def get_number(self):
        return self._number


class Aircraft:

    def __init__(self, registration , model , num_rows , num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def get_registration(self):
        return self._registration

    def get_model(self):
        return self._model

    def seating_plan(self):
        return (range(1,self._num_rows+1),"ABCDEFGHJK"[:self._num_seats_per_row])    ## Returns a tuple


a = Aircraft("G-EUPT","Airbus A319",num_rows = 10,num_seats_per_row = 6)

print(a.seating_plan())
