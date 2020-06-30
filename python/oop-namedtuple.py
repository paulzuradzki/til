"""Demonstrates how a namedtuple can be used as a "mini" class for storing data attributes.

You will still need classes to implement methods.

"""

# note use of __class__.__name__ to avoid repeating class name in repr string
# str() will also call __repr__ by default if __str__ is not implemented

class Auto():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def __repr__(self):
        return f"{self.__class__.__name__}(make={self.make}, model={self.model}, year={self.year})"
    
mycar = Auto(make='Honda', model='Civic', year=2018)

print(mycar)
print(mycar.make)
print(mycar.model)
print(mycar.year)
print(repr(mycar))

# represent these attributes using named tuple `AutoNT`
from collections import namedtuple

AutoNT = namedtuple('Auto', ['make', 'model', 'year'])
mycar2 = AutoNT(make='Toyota', model='Corolla', year=2020)

print(mycar2)
print(mycar2.make)
print(mycar2.model)
print(mycar2.year)
print(repr(mycar2))
