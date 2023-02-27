"""
SQLlite
"""


import sqlite3

conn = sqlite3.connect(':memory:') # In-memory db Useful for testing, Creates fresh DB on every run

# Persist data on db file within the connect method
# conn = sqlite3.connect('employee.db') 

# cursor allows to execute SQL commands
c = conn.cursor()  

# Creating Employee table.
c.execute("""CREATE TABLE employees (
            first TEXT,
            last TEXT,
            pay INTEGER
            )""")

# c.execute("INSERT INTO employees VALUES ('Errol','Vas',70000)")

# conn.commit()
# c.execute("SELECT * FROM employees WHERE ")


# fetchone() - One row or fetchmany(x) - requires x rows , fetchall() 
# print(c.fetchone())   # REturs the tuple

# print(c.fetchall())   # Returns a list of all records as list of tuple records.


# Commits the current transaction
# conn.commit()  

# Close the connection
# conn.close()


# Using the class from employee module
from employee import Employee

emp_1 = Employee('John','Doe',80000)
emp_2 = Employee('Mary','Doe',90000)

## BAD!! SQL INJECTION ATTACKS : Instead use question marks DB API placeholders
# c.execute("INSERT INTO employees VALUES ('{}' , '{}', '{}')".format(emp_1.first, emp_1.last, emp_1.pay) 

# conn.commit()  

# # 1st method
# c.execute("INSERT INTO employees VALUES (?, ?, ?)",(emp_1.first, emp_1.last, emp_1.pay)) 

# conn.commit()  


# # 2nd method
# c.execute("INSERT INTO employees VALUES (:first, :last, :pay)",{'first':emp_2.first,'last': emp_2.last,'pay': emp_2.pay}) 

# conn.commit()  


c.execute("SELECT * FROM employees WHERE last=?",('Vas',))


print(c.fetchall())

c.execute("SELECT * FROM employees WHERE last=:last",{'last':'Doe'})

print(c.fetchall())

conn.commit()  

# Close the connection
conn.close()


# Helper fnctions

def insert_employee(emp):
    # No need commit. Use context manager.
    with conn:
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)",{'first':emp.first,'last': emp.last,'pay': emp.pay}) 


def get_emp_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last",{'last':lastname})
    return c.fetchall()


def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                WHERE first= :first AND last = :last""",
                {'first':emp.fist,
                'last': emp.last,
                'pay':emp.pay})



def remove_emp(emp):
    with conn:
        c.execute("""DELETE FROM employees WHERE first= :first AND last = :last""",
                {'first':emp.fist,
                'last': emp.last})

        

insert_employee(emp_1)