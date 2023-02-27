#######################
# Persisting data on disk
#######################
"""
SErializing and Deserializing of data

pickle : 

Use a cryptographic signature to ensure that your pickled data has not been tampered with.


IMPORTANT!!!
Unpickling erroneous or malicious data from an untrusted source can be dangerou


dump and load to convert Python objects to and form stream files.
dumps and loads to convert into byte objects.

In day-to-day applications, pickle is usually used when we need to persist Python data that is not supposed to be exchanged with another application.
Example : The session manager in a flask plugin, which pickles the session object before storing it in a Redis database.


shelve : ( when sort on resources)

SQL alchemy:
A shelf is a persistent dictionary-like object

"""
import pickle
from dataclasses import dataclass

@dataclass
class Person:
    first_name : str
    last_name: str
    id_: int

    def greet(self):
        print("I am {} {} and my ID is {}".format(self.first_name, self.last_name, self.id_))

people = [Person('Popye','Sailor', 123), 
            Person('Johnny','Bravo', 2323)]

# Saving as a binary file.
with open('data.pickle','wb') as stream:
    # pickle.dump(obj, file)
    print("Saving the file as binary...")
    pickle.dump(people,stream)
    print("Saved Successfully")

# Loading the data from file into stream
with open('data.pickle','rb') as stream:
    print("Loading the byte file...")
    peeps = pickle.load(stream)

for item_ in peeps:
    item_.greet()


