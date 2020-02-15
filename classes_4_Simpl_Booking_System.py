# Classes : Simple Booking System
from pprint import pprint as pp

class Flight:
    """ A model for a flight with aircraft"""
    def __init__(self, number , aircraft):

        if not number[:2].isalpha():
            raise ValueError("Invalid Airline code in {}".format(number))

        if not number[:2].isupper():
            raise ValueError("Invalid flight number in {}".format(number))

        if not number[2:].isdigit() and int(number[2:] <= 9999) :
            raise ValueError("Invalid route code in {}".format(number))

        self._number = number
        self._aircraft = aircraft

        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{seat:None for seat in seats} for _ in rows]

    def get_airline(self):
        return self._number[:2]

    def get_number(self):
        return self._number[2:]

    def get_airplane_model(self):
        return self._aircraft.get_model()

    def allocate_seat(self, seat, passenger_name):
        """ Allocate a seat to a passenger.

        Args:
            seat: Seat number like '12C' , '32W'.
            passenger : Name of the passenger_name

        Raises:
            ValueError : If the seat is already taken"""

        rows, seat_letters = self._aircraft.seating_plan()

        letter =  seat[-1]
        if letter not in seat_letters:
            raise ValueError("Invalid seat letter in {}".format(seat))

        row_number = seat[:2]
        try:
            row = int(row_number)                       # Converting the row number to int
        except ValueError:
            raise ValueError("Invalid seat row in {}".format(seat))

        if row not in rows:
            raise ValueError("Invalid row number {}".format(row))    # The entered row is not in the row list

        if self._seating[row][letter] is not None:
            raise ValueError("Seat {} already occupied".format(seat))   # The seat is already occupied

        self._seating[row][letter] = passenger_name


class Aircraft:
    """A model aircraft with registration, model , number of rows and number of seats per row"""
    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def get_registration(self):
        return self._registration

    def get_model(self):
        return self._model

    def seating_plan(self):
        return (range(1,self._num_rows+1),"ABCDEFGHJK"[:self._num_seats_per_row])

Air1 = Flight("IG6766",Aircraft("IG-1930","Airbus-567",num_rows = 10,num_seats_per_row=5))

print(Air1.get_airline())
print(Air1.get_number())
print(Air1.get_airplane_model())
pp(Air1._seating)

pp(Air1.allocate_seat('05B','Darryl'))
pp(Air1._seating)
pp(Air1.allocate_seat('03B','Xacn'))
pp(Air1._seating)
pp(Air1.allocate_seat('11q','Xaasdcn'))
