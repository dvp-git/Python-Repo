# Classes : Simple Booking System with re-location
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

    def _parse_seat(self,seat):               # Underscore because it is implementation detail
        """ Parse a seat designator into a valid row and seat_letter

        Args:
            seat: A seat disgnator such as '12F'

        Returns:
            A tuple containing an integer and a string for row & seat respectivel"""

        rows, seat_letters = self._aircraft.seating_plan()

        letter =  seat[-1]
        if letter not in seat_letters:
            raise ValueError("Invalid seat letter in {}".format(seat))

        row_number = seat[:-1]
        try:
            row = int(row_number)                       # Converting the row number to int
        except ValueError:
            raise ValueError("Invalid seat row in {}".format(seat))

        if row not in rows:
            raise ValueError("Invalid row number {}".format(row))    # The entered row is not in the row list

        return row, letter

    def allocate_seat(self, seat, passenger_name):
        """ Allocate a seat to a passenger.

        Args:
            seat: Seat number like '12C' , '32W'.
            passenger : Name of the passenger_name

        Raises:
            ValueError : If the seat is already taken"""

        row , letter = self._parse_seat(seat)

        if self._seating[row][letter] is not None:
            raise ValueError("Seat {} already occupied".format(seat))   # The seat is already occupied

        self._seating[row][letter] = passenger_name


    def relocate_passenger(self, from_seat, to_seat):
        """ Relocate passenger from 'from_seat' to 'to_seat'

        Args:
            from_seat: The existing passenger to be moved
            to_seat: The new seat to be designated"""

        from_row,from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError("No passenger to relocate in seat {}".format(from_seat))

        to_row,to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError("Seat {} is already occupied".format(to_seat))

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None

    def seats_availble(self):
        return sum(sum(1 for s in row.values() if s is None)    # Outer expresion filters for all rows which are not None i.e.it excludes the dummy first row, and inner expression iterates over each value of the dictionary in each row and adds 1 if a None is found
                        for row in self._seating
                        if row is not None)


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




def make_flight():
    Air1 = Flight("IG6766",Aircraft("IG-1930","Airbus-567",num_rows = 20,num_seats_per_row=6))
    Air1.allocate_seat('12A','Guido Van Rossum')
    Air1.allocate_seat('15F','Bjarne Stroustrup')
    Air1.allocate_seat('15E','Ander Hejlsberg')
    Air1.allocate_seat('1C','John McCarthy')
    Air1.allocate_seat('1D','Richard Hickey')
    return Air1

Air1 = make_flight()

pp(Air1._seating)

Air1.relocate_passenger('12A','15D')

pp(Air1._seating)
print(Air1.seats_availble())
