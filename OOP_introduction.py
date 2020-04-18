class Account():
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder

a = Account('Jim')
print(a.balance)
print(a.holder)

class Account(obeject):
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance
    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance

test_class = Account('Hu')
test_class.holder = 'Zhao'
print(test_class.holder)
getattr(test_class, 'holder')
hasattr(test_class, 'holder')

def make_instance(cls):
    def get_value(name):
        if name in attributes:
            return attributes[name]
        else:
            value = cls['get'](name)
            return bind_method(value, instance)
    def set_value(name, value):
        attributes[name] = value
    attributes = {}
    instance = {'get' : get_value, 'set' : set_value} # this is beautiful
    return instance

def bind_method(value, instance):
    if callable(value):
        def method(*args):
            return value(instance, *args)
        return method
    else:
        return value

from datetime import date
today = date(2011, 9, 12)
repr(today)
str(today)

from math import atan2
class ComplexRI(object):
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    @property
    def magnitude(self):
        return (self.real ** 2 + self.imag ** 2) ** 0.5
    @property
    def angle(self):
        return atan2(self.imag, self.real)
    def __repr__(self):
        return 'ComplexRI_hu({0}, {1})'.format(self.real, self.imag)

test_complex = ComplexRI(1, 5)
print(test_complex.magnitude)
print(repr(test_complex))

from fractions import gcd
class Rational(object):
    def __init__(self, numer, denom):
        g = gcd(numer, denom)
        self.numer = numer // g
        self.denom = denom // g
    def __repr__(self):
        return 'Rational({0}, {1})'.format(self.numer, self.denom)

def type_tag(x):
    return type_tag.tags[type(x)]
type_tag.tags = {ComplexRI: 'com', ComplexMA: 'com', Rational: 'rat'}