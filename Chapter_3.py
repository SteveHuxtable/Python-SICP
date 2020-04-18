def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) - fib(n-2)

print(fib(3))

def memo(f):
    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized
fib = memo(fib)
fib(40)

class Rlist(object):
    class EmptyList(object):
        def __len__(self):
            return 0
    empty = EmptyList() # define an empty list
    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest
    def __repr__(self):
        '''recursion'''
        args = repr(self.first)
        print(args)
        if self.rest is not Rlist.empty:
            args += ', {0}'.format(repr(self.rest))
        return 'Rlist({0})'.format(args)
    def __len__(self):
        '''recursion'''
        return 1 + len(self.rest)
    def __getitem__(self, i):
        '''usage: s[i]'''
        '''recursion'''
        if i == 0:
            return self.first
        return self.rest[i-1]

s = Rlist(1, Rlist(2, Rlist(3)))

def extend_list(s1, s2):
    if s1 == Rlist.empty:
        return s2
    return Rlist(s1, extend_list(s1.rest, s2))

def map_rlist(s, fn):
    if s is Rlist.empty:
        return s
    return Rlist(fn(s.first), map_rlist(s.rest, fn))

def filter_rlist(s, fn):
    if s is Rlist.empty:
        return s
    rest = filter_rlist(s.rest, fn)
    if fn(s.first):
        return Rlist(s.first, rest)
    return rest

class Tree(object):
    def __init__(self, entry, left=None, right=None):
        self.entry = entry
        self.left = left
        self.right = right
    def __repr__(self):
        args = repr(self.entry)
        if self.left or self.right:
            args += ', {0}, {1}'.format(repr(self.left), repr(self.right))
        return 'Tree({0})'.format(args)

s = {1, 2, 3, 4, 5}

try:
    x = 1/0
    print(x)
except ZeroDivisionError as e:
    print('handling a', type(e))
    str(e)
    x = 0

class Exp(object):
    def __init__(self, operator, operands):
        self.operator = operator
        self.operands = operands
    def __repr__(self):
        return 'Exp({0}, {1})'.format(repr(self.operator), repr(self.operands))
    def __str__(self):
        operands_strs = ', '.join(map(str, self.operands))
        return '{0}({1})'.format(self.operator, operands_strs)

from operator import mul
from functools import reduce
def calc_apply(operator, args):
    if operator in ('add', '+'):
        return sum(args)
    if operator in ('sub', '-'):
        if len(args) == 0:
            raise TypeError(operator + 'requires at least 1 argument')
        if len(args) == 1:
            return -args[0]
        return sum(args[:1] + [-arg for arg in args[1:]])
    if operator in ('mul', '*'):
        return reduce(mul, args, 1)
    if operator in ('div', '/'):
        if len(args) != 2:
            raise TypeError(operator + ' requires exactly 2 arguments')
        numer, denom = args
        return numer/denom

calc_apply('div', (1, 0, 3))

def read_eval_print_loop():
    while True:
        expression_tree = calc_parse(input('calc> '))
        print(calc_eval(expression_tree))

def calc_parse(line):
    tokens = tokenize(line)
    expression_tree = analyze(tokens)
    if len(tokens) > 0:
        raise SyntaxError('Extra token(s):' + ' '.join(tokens))
    return expression_tree

def tokenize(line):
    spaced = line.replace('(', ' ( ').replace(')', ' ) ').replace(',', ' , ')
    print(type(spaced))
    spaced = spaced.split()
    print(type(spaced))
    return spaced