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

def try_illustrate(a, b):
    """ have a try to use the illustration
    """
    print(a + b)

help(try_illustrate)
try_illustrate(1, 3)

def absolute_value(a):
    """ Get the absolute value

    abs(a)
    """
    if a >= 0:
        print(a)
    else:
        print(-a)

absolute_value(1)
absolute_value(0)
absolute_value(-0)
absolute_value(-1)

print(True and False)

def fib(n):
    """Fibonacci sequence

    to get the Nth value in a Fibonacci sequence                            

    n -- the Nth element
    """
    prev, curr = 0, 1
    k = 2
    while k < n:
        prev, curr = curr, prev + curr
        k = k + 1
    return curr
fib(8)

def fib_test():
    """ To test the accuracy of func fib()"""
    assert fib(1) == 1, 'fib(1) should be 1'
    assert fib(2) == 1, 'fib(1) should be 1'
    assert fib(12) == 1, 'fib(12) should not be 1'
fib_test()

def summation(n ,term, next):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), next(k)
    return total
def cube(k):
    return pow(k, 3)
def successor(k):
    return k + 1

def sum_cubes(n):
    return summation(n, cube, successor)
sum_cubes(3)

def iter_improve(update, test, guess = 1):
    while not test(guess):
        guess = update(guess)
    return guess

def near(x, f, g):
    return approx_eq(f(x), g(x))

def approx_eq(x, y, tolerance = 1e-5):
    return abs(x - y) < tolerance

def golden_update(guess):
    return 1/guess + 1

def golden_test(guess):
    return near(guess, square, successor)

iter_improve(golden_update, golden_test)

def average(a, b):
    return (a + b)/2

average(1, 2)

def square_root(x):
    def update(guess):
        return average(guess, x/guess)
    def test(guess):
        return approx_eq(square(guess), x)
    return iter_improve(update, test)

square_root(9)