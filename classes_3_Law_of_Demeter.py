### The Law of Demeter : Secondary Class


class Flight:
    """ Model for a Flight with a passenger Aircraft"""
    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError("No airplane code in {}".format(number))

        if not number[:2].isupper():
            raise ValueError("Invalid Airline code in {}".format(number))

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError("Invalid Route code in {}".format(number))

        self._number = number
        self._aircraft = aircraft   # Adding a attribute to store the AirCraft Object

    def get_number(self):
        return self._number

    def get_airline(self):
        return self._number[:2]

    def get_aircraft_model(self):
        return self._aircraft.get_model()  # Adding a method to report the aircraft model. This method delegates to aircraft on behalf of the client rather than the client to reach through the Flight and interrogate the 'aircraft' object directly.

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
        return (range(1,self._num_rows+1),"ABCDEFGHJK"[:self._num_seats_per_row])   ## Returns a tuple


f = Flight("SN1034",Aircraft("G-EUPT","Airbus A319",num_rows = 10,num_seats_per_row = 6))

print("get_number",f.get_number())
print("get_airline",f.get_airline())
print("get_aircraft_model",f.get_aircraft_model())
