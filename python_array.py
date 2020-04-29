import sys
data = []
n = 20
for k in range(n):
    a = len(data)
    b = sys.getsizeof(data)
    print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
    data.append(None)


import ctypes

class DynamicArray:
    '''A dynamic array class akin to a simplified Python list.'''

    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if not 0 <= k < self._n:
            raise IndexError('Invalid index')
        return self._A[k]

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        return (c * ctypes.py_object)()

test_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(test_list.pop())
print(test_list.pop(0))
print(test_list)

test_list = [k*k for k in range(1, 20, 2)]
print(test_list)

document = 'hhhhhhhu'
temp = []
for c in document:
    if c.isalpha():
        temp.append(c)
letters = ''.join()

[c for c in document if c.isalpha()]
letters = ''.join(c for c in document)

generator_ex = (x*x for x in range(10))
print(next(generator_ex))

for i in generator_ex:
    print(i)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

a = fib(10)

for b in fib(10):
    print(b)

test_list = [1, 2, 3, 4, 5, 6]
i = iter(test_list)
for j in i:
    print(j)

data = [[0] * 4 for j in range(5)]

class ArrayStack:

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()