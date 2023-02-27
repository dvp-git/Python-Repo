######################
""" OOPS , Classes """
######################
"""
1. Class attributes are shared among all instances, while instance attributes are not;
therefore, you should use class attributes to provide the states and behaviors to be shared by all instances 
and use instance attributes for data that will be specific to each individual object.


2. The first argument will always be the instance: "self" that the method will be bound to. We don't need to necessarily call it self, 
but it's the convention, and this is one of the few cases where it's very important to abide by it. Similarly for @classmethod cls is the first arguement.

3. initializer __init__: 
Ex: p1.net_price = 100
An initializer,( executes when object is created) since it works on an already created instance, and therefore it's called __init__.

4. constructor __new__ : Used when writing metaclasses/ *******Advacned topic*******

5. super() is a function that returns a proxy object that delegates method calls to a parent or sibling class. 

super().__init__(<attributed of Base Class to be assigned to dervied class>). During multiple inheritance, the first class is checked:
DerviedClass(Base1, Base2) - Base1 attributes initialized, followed by Base2 in dervied class

6. Method Resolution Order : If multiple inheridtance exists.

__class.__.__mro__


"""

# class Person():
#     species = "Human"

# Person.alive = True # Addding class attribute dynamically 

# person_1 = Person()


# print(person_1.alive , person_1.species) #Inherited from class
#     #Inherited from class 


# person_1.name = "Darryl"  # added instance attributes dynamically 
# person_1.place = "USA"    # added instance attributes dynamically
# print(person_1.name, person_1.place)



"""The self argument

self : the first attribute of an instance method. 


"""

# class Square():
#     side = 8
#     def area():  
#         return Square.side ** 2   # Calling explicitly  - Class.attribute 

# Square.area()  # 64 


# class Square():
#     side = 8
#     def area(self):  # self is a reference to an instance of the class Square()
#         return self.side ** 2

# sq = Square()
# print(sq.area())   # prints Sqaure.side * Square.side = 8 * 8 = 64 , NOTE: Square.area(sq) and sq.area() are equivalent 


# # Now change the instances side attribute
# sq.side = 16  
# print(sq.area())  # prints 16 * 16  = 256
 



""" Declaring instance attributes as arguments in initialization"""
# class Rectangle:
#     def __init__(self, side_a, side_b):
#         self.side_a = side_a
#         self.side_b = side_b
#     def area(self):
#         return self.side_a * self.side_b
# r1 = Rectangle(10, 4)
# print(r1.side_a, r1.side_b)  # 10 4
# print(r1.area())  # 40
# r2 = Rectangle(7, 3)
# print(r2.area())  # 21

# Rectangle.side_ac = 5  # Dynamically assigned attribute

# p1 = Rectangle(10, 4)
# p1.side_a
# p1.side_ac    #Inherited dynamically assigned attribute class 


"""
Inheritance : 2 objects are related by means of an Is-A type of relationship. 

class ClassB(BaseClassName):
     pass

# If you don't specify a base class, brackets are optional and in practice are never used.
# Python will set the special "object" class as the base class for the one we're defining

Composition : 2 two objects are related by means of a Has-A type of relationship

class ClassB():
    attrib = ClassA
    def __init__(self):
        self.<attribute> = self.attrib()  # ClassB has a ClassA attribute in it.

Eg:
Car Has-A Engine. 
Different types of engines. V8Engine Is-A Engine.
"""

#########################################################################################
# Inheritance and Composition
#########################################################################################

# class Engine:
#     def start(self):
#         print("{} class started".format(self.__class__.__name__))

#     def stop(self):
#         print("{} class stopped".format(self.__class__.__name__))

# class ElectricEngine(Engine):  # Is-A Engine
#     pass

# class V8Engine(Engine):  # Is-A Engine
#     pass


# class Car:
#     engine_cls = Engine  
#     def __init__(self):
#         self.engine = self.engine_cls() # Car class Has-A Engine class

#     def start(self):
#         print(
#             'Starting engine {} for {}'.format(self.engine.__class__.__name__, self.__class__.__name__)
#         )
#         self.engine.start()

#     def stop(self):
#         print(
#             'Stopping engine {} for {}'.format(self.engine.__class__.__name__, self.__class__.__name__)
#         )
#         self.engine.stop()
    
    
# class RaceCar(Car):  # Is-A Car
#     engine_cls = V8Engine


# class CityCar(Car):  # Is-A Car
#     engine_cls = ElectricEngine


# class F1Car(RaceCar):  # Is-A RaceCar and also Is-A Car
#     pass  # engine_cls same as parent

# # Instantiate the classes

# car = Car()
# raceCar = RaceCar()
# cityCar = CityCar()
# f1Car = F1Car()

# # Testing start
# cars = [car, raceCar, cityCar]
# for car in cars:
#     print(car.start())

# # Testing correctnes of instantiated cars

# cars_list = [(car,'car'),(raceCar,'raceCar'),(cityCar,'cityCar'),(f1Car,'f1Car')]
# classList = [Car, RaceCar,CityCar]

# for clss in classList:
#     for c,k in cars_list:
#         if isinstance(c, clss):
#             print("{} is instance of {}".format(k,clss.__name__))
#         else:
#             print("{} is not instance of {}".format(k,clss.__name__))


########################################################
# Accessing BaseClass from the derivedClass
########################################################
class Book():
    def __init__(self, title, publisher, pages):
        self.title = title
        self.publisher = publisher
        self.pages = pages    
        self.number = 123  # These attributes become part of Ebook object even if Ebook class is not touched
        self.acid = "acid" # These attributes become part of Ebook object even if Ebook class is not touched
 

    
class Ebook(Book):
    """ Bad practice: since if Book attributes are changed,
      Ebook won't reflect due to re-defining. Only Child __init__ is called. Errors due to change in base class attributes"""
    # def __init__(self, title, publisher, pages, format_):
    #     self.title = title
    #     self.publisher = publisher
    #     self.pages = pages
    #     self.format_ = format_

    #     >>> ebook.number
    # Traceback (most recent call last):
    #   File "<stdin>", line 1, in <module>
    # AttributeError: 'Ebook' object has no attribute 'number'

    """Use this instead to inherit __init__"""
    def __init__(self, title, publisher, pages,format_):
        # Passed variables from Ebook object to Book class. If Book __init__ method changes, all __init__ of Book becomes part of Ebook
        Book.__init__(self, title, publisher, pages)  
        self.format_ = format_

ebook = Ebook(
    'Learn Python Programming', 'Packt Publishing', 500, 'PDF')
print(ebook.title)  # Learn Python Programming
print(ebook.publisher)  # Packt Publishing
print(ebook.pages)  # 500
print(ebook.format_)  # PDF
print(ebook.number)  # 123 
print(ebook.acid)    # acid


"""
super() is a function that returns a proxy object that delegates method calls to a parent or sibling class.
Useful if the Base Class name is changed over time.
"""
# Use super() for inheriting Base class __init__

class Ebook(Book):
    
    def __init__(self, title, publisher, pages,format_):
        # Using super()
        super().__init__(title, publisher, pages)  
        self.format_ = format_

ebook = Ebook(
    'Learn Python Programming', 'Packt Publishing', 500, 'PDF')
print(ebook.title)  # Learn Python Programming
print(ebook.publisher)  # Packt Publishing
print(ebook.pages)  # 500
print(ebook.format_)  # PDF
print(ebook.number)  # 123 
print(ebook.acid)    # acid



################################################################################
"""Method Resolution Order MRO""" 
################################################################################
"""
object.__class__.__mro__
When object atttribute is searched Python will search the class where it was defined up to base class( if inherited ). 
If class had multiple inheritence, MRO is used to know which classes are searched for attribute lookup.
"""
class A:
    label = 'a'
class B(A):
    pass  # was: label = 'b'
class C(A):
    label = 'c'
class D(B, C):
    pass
d = D()
print(d.label)  # 'c'
print(d.__class__.mro())  # notice another way to get the MRO
# prints:
# [<class '__main__.D'>, <class '__main__.B'>,
# <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

