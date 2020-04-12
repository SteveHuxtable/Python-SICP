from urllib.request import urlopen
from operator import mul, add, sub
# shakespeare = urlopen('http:// inst.eecs.berkeley.edu/~cs61a/fa11/shakespeare.txt')
# words = set(shakespeare.read().decode().split())

print(max(1, 10))
print(pow(3, 2))

a, b = 10, 100
print(a)

print(add(10, sub(2, 1)))
print(print(10)) # output: None

def square(x):
    return mul(x, x)

print(square(10))

# write a closure
def Closure1():
    item = 10
    return lambda: print(item)
test_closure = Closure1()
test_closure()

def new_counter():
    i = 0
    def add_one():
        nonlocal i
        i = i + 1
        print(i)
    return add_one
first_counter = new_counter()
first_counter()
first_counter()