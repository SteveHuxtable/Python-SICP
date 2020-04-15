from datetime import date
today = date(2020, 4, 13)
print(today.day)

type(today)
print(today.strftime('%A, %B %d'))

pair = (1, 2)
x, y = pair
print(x)
print(y)
print(pair[0])
print(pair[1])

from operator import getitem
print(getitem(pair, 0))

def make_rat(n, d):
    return (n, d)
def numer(x):
    return getitem(x, 0)
def denom(x):
    return getitem(x, 1)
def str_rat(x):
    return '{0}/{1}'.format(numer(x), denom(x))

test_rat = make_rat(2, 4)
print(str_rat(test_rat))

from math import gcd
def make_rat2(n, d):
    g = gcd(n, d)
    return(n // g, d // g)

test_rat2 = make_rat2(2, 4)
print(str_rat(test_rat2))

def add_rat(x1, x2):
    new_rat_numer = numer(x1) * denom(x2) + numer(x2) * denom(x1)
    new_rat_denom = denom(x1) * denom(x2)
    new_rat = make_rat2(new_rat_numer, new_rat_denom)
    return new_rat

half = make_rat2(1, 2)
quarter = make_rat2(1, 4)
print(str_rat(add_rat(half, quarter)))

def make_pair(x, y):
    ''' this is a closure '''
    def dispatch(m):
        if m == 0:
            return x
        elif m == 1:
            return y
    return dispatch
def getitem_pair(p, i):
    return p(i)

test_rat3 = make_pair(1, 2)
print(getitem_pair(test_rat3, 0))

empty_rlist = None
def make_rlist(first, rest):
    return (first, rest)
def first(s):
    return s[0]
def rest(s):
    return s[1]

counts = make_rlist(1, make_rlist(2, make_rlist(3, make_rlist(4, empty_rlist))))
print(first(counts))
print(rest(counts))

def len_rlist(s):
    '''iteration'''
    length = 0
    while s != empty_rlist:
        s, length = rest(s), length + 1
    return length
def getitem_rlist(s, i):
    '''iteration'''
    while i > 0:
        s, i = rest(s), i - 1
    return first(s)
def len_rlist_recur(s):
    '''recursion'''
    length = 0
    if s == empty_rlist:
        return length
    else:
        return len_rlist_recur(rest(s)) + 1
        

len_rlist(counts)
len_rlist_recur(counts)

digits = (1, 8, 2, 8)
print(len(digits))
print(digits[3])

negative_list = (-1, -2, -3, -4, -5)
print(tuple(map(abs, negative_list)))

def count(s, value):
    total = 0
    for elem in s:
        if elem == value:
            total += 1
    return total

s = [1, 2, 3, 4, 5, 6, 6, 7]
s2 = (1, 2, 3, 4, 5, 6, 6, 7)
print(count(s, 6))
print(count(s2, 6))
s[0] = 0
s2[0] = 0

pairs = ((1, 2), (3, 4), (5, 6), (7, 8), (5, 5))
def count_same_pair(pairs):
    same_count = 0
    for x, y in pairs:
        if x == y:
            same_count += 1
    return same_count
print(count_same_pair(pairs))

i = 0
for _ in range(10):
    print(i)
    i += 1

import re
line = "Mississippi 12345"
patt = r'issi'
pattern = re.compile(patt)
result = pattern.findall(line)

line="this hdr-biz model args= server"
patt=r'server'
pattern = re.compile(patt)
result = pattern.findall(line)

def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(20))

def iseven(x):
    return x % 2 == 0

nums = [1, 2, 3, 4, 5, 6, 7, 8]
print(tuple(filter(iseven, nums)))
print(sum(nums))
