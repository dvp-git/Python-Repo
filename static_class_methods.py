######################
""" STATIC AND CLASS METHODS """
######################

######################
# Static Method : @staticmethod
######################
class StringUtil:
    
    @staticmethod
    def is_palindrome(s, case_insensitive=True):
        s = ''.join(c for c in s if c.isalnum())
        if case_insensitive:
            s = s.lower()
        for c in range(len(s)//2):
            if s[c] != s[-c-1]:
                return False
        return True

    @staticmethod
    def get_unique_words(sentence):
        sentence = sentence.split()
        return set(sentence)


print(StringUtil.is_palindrome("AABAA"))
print(StringUtil.is_palindrome(
    'In Girum Imus Nocte Et Consumimur Igni')  # Latin! Show-off!
)  # True
print(StringUtil.get_unique_words(
    'I love palindromes. I really really love them!'))


"""
Class methods: @classmethod
A very common use case for coding class methods is to provide factory capability to a class,
which means to have alternative ways to create instances of the class.

Takes an additional argument which is the "class object" itself
"""
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_tuple(cls, coords):
        return cls(*coords)  # Tuple unpacking

    @classmethod
    def from_point(cls, point):
        return cls(point.x, point.y)  # Passing the points

p = Point.from_tuple((3,7))    # Same as p = Point(3,7)
print("{}".format(p)) # <__main__.Point object at 0x00000249746883a0>p

print(p.x , p.y)  # 3, 7

q = Point.from_point(p)
print(q.x, q.y)



""" Sepcial case: Calling class meethod """
# # Base class : Engine
# class Engine():
#     @classmethod
#     def start(cls):
#         print(f"Starting {cls.__name__} Engine...")
#         pass

#     @classmethod
#     def stop(cls):
#         print(f"Stopping {cls.__name__} Engine...")
#         pass

#     def start_o(self):
#         print(f"Starting {self.__class__.__name__} Engine...")
#         pass

#     def stop_o(self):
#         print(f"Starting {self.__class__.__name__} Engine...")
#         pass

# class ElectricEngine(Engine):  # Is-A Engine
#     pass
# class V8Engine(Engine):  # Is-A Engine
#     pass

# # Methods to instance of the class
# a = Engine()
# a.start_o()

# # Methods calls on the class itself
# print(ElectricEngine.stop())
# print(V8Engine.stop())

##############################################################
"""Private Methods and name mangling"""
##############################################################
"""
public: If an attribute's name has no leading underscores.

private: One leading underscore. Meant to be private. Don't modify or call it. Eg: helper methods


Name mangling means that any attribute name that has at least two leading underscores and at most one trailing underscore, such as __my_attr, 
is replaced with a name that includes an underscore and the class name before the actual name, such as _ClassName__my_attr.

Designing a library with classes that are meant to be used and extended by other developers. Important


"""
# class A:
#     def __init__(self, factor):
#         self._factor = factor
#     def op1(self):
#         print('Op1 with factor {}...'.format(self._factor))
# class B(A):
#     def op2(self, factor):
#         self._factor = factor
#         print('Op2 with factor {}...'.format(self._factor))
# obj = B(100)
# obj.op1()    # Op1 with factor 100...
# obj.op2(42)  # Op2 with factor 42...
# obj.op1()    # Op1 with factor 42... <- This is BAD , factor of class A is changed here.
# print(obj.__dict__.keys())    #  dict_keys(['_factor'])

# # Fix : 
# # double leading underscore -- > replaced as _ClassName__my_attr
# class A:
#     def __init__(self, factor):
#         self.__factor = factor
#     def op1(self):
#         print('Op1 with factor {}...'.format(self.__factor))
# class B(A):
#     def op2(self, factor):
#         self.__factor = factor
#         print('Op2 with factor {}...'.format(self.__factor))
# obj = B(100)
# obj.op1()    # Op1 with factor 100...
# obj.op2(42)  # Op2 with factor 42...
# obj.op1()    # Op1 with factor 100... <- Wohoo! Now it's GOOD!
# print(obj.__dict__.keys())    # dict_keys(['_A__factor', '_B__factor'])

##################
# @property : Use the method names as if they were attributes
# Accesors :

##################
# class Person:
#     def __init__(self, age):
#         self.age = age  # anyone can modify this freely
# class PersonWithAccessors:
#     def __init__(self, age):
#         self._age = age
#     def get_age(self):
#         return self._age
#     def set_age(self, age):
#         if 18 <= age <= 99:
#             self._age = age
#         else:
#             raise ValueError('Age must be within [18, 99]')

#  # Pythonic : any variable acessing age is subject to @property and            
# class PersonPythonic:
#     def __init__(self, age):
#         self._age = age

#     @property
#     def age(self):
#         return self._age

#     @age.setter
#     def age(self, age):
#         # if 18 <= age <= 99:
#         #     self._age = age
#         # else:
#         #     raise ValueError('Age must be within [18, 99]')
#         print("NO ACCESS")


# person = PersonPythonic(39)
# print(person.age)  # 39 - Notice we access as data attribute
# person.age = 42    # Notice we access as data attribute
# print(person.age)  # 42
# person.age = 100   # NO ACCESS

#############################################
# @cached_property
"""
Used when we need to cache something
"""
#############################################
class Client():
    def __init__(self):
        print("Creating Client from {} class".format(self.__class__.__name__))

    def run_query(self,**kwargs):
        print("Perfoming query:{}".format(kwargs))

class Manager():
    @property
    def client(self):
        return Client()

    def query(self, **kwargs):
        return self.client.run_query(**kwargs)

# c = Manager()
# >>> c.query(d="SELECT * FROM customer") 
# Creating Client from Client class
# Perfoming query:{'d': 'SELECT * FROM customer'}

class ManualCacheManager():
    @property
    def client(self):
        # If Client() is created once, no need to create again when query is run
        if not hasattr(self,'_client'):
            self._client = Client()
        return self._client

    def query(self, **kwargs):
        return self.client.run_query(**kwargs)


# >>> a.query(id_1 = "SELECT 1")
# Creating Client from Client class
# Perfoming query:{'id_1': 'SELECT 1'}
# >>> a.query(id_2 = "SELECT 2")
# Perfoming query:{'id_2': 'SELECT 2'}


######################################################
#cached_property
#####################################################
# from functools import cached_property
# class CachedPropertyManager:
#     @cached_property
#     def client(self):
#         return Client()
#     def query(self, **kwargs):
#         return self.client.run_query(**kwargs)

# manager = CachedPropertyManager()
# manager.query(object_id=42)
# manager.query(name_ilike='%Python%')
# del manager.client  # This causes a new Client on next call
# manager.query(age_gte=18)

# >>> manager.query(object_id=42)
# Creating Client from Client class
# Perfoming query:{'object_id': 42}
# >>> manager.query(name_ilike='%Python%')
# Perfoming query:{'name_ilike': '%Python%'}
# >>> del manager.client  # This causes a new Client on next call
# >>> manager.query(age_gte=18)
# Creating Client from Client class
# Perfoming query:{'age_gte': 18}