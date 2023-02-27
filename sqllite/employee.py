""" Class for employee """
class Employee():
    """ Sample class for an employee"""

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last 
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


    def __repr__(self):
        return "Employee('{}'.'{}','{}')".format(self.first, self.last, self.pay)

# a = Employee('Ddr','EES',23)
# print(a.email)