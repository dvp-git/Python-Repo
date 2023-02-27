#############################
# SQLAlchemy
#############################
"""
In-memory ORM : sqlalchemy


Object-Relational Mapping (ORM) : Regardless of the flavour of SQL , maps objects of programming language to a relational database. Most commonly used. 
If unable to then resort to using SQL directly.


"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column, Integer, String, ForeignKey, create_engine)
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///:memory:') # Create the DB engine, or type of db we have chosen
Base = declarative_base()                   # Base table. 

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    addresses =  relationship(
        'Address',
        back_populates='person',
        order_by='Address.email',
        cascade='all,delete-orphan'
    )

    def __repr__(self):
        return "{}(id={})".format(self.name,self.id)

class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    person_id = Column(ForeignKey('person.id'))
    person = relationship(
        'Person',
        back_populates='addresses')

    def __str__(self):
        return self.email

    __repr__ = __str__


Base.metadata.create_all(engine)

