class Positives(object):
    def __init__(self):
        self.current = 0
    def __next__(self):
        result = self.current
        self.current += 1
        return result
    def __iter__(self):
        return self

counts = [1, 2, 3]
for item in counts:
    print(item)

i = iter(counts)
try:
    while True:
        item = next(i)
        print(item)
except StopIteration:
    pass

try:
    fp = open("sample.txt")
except IOError as e:
    print('Unable to do this!: ', e)
    '''re-raise the error'''
    raise

test_list = [1, 2, 3, 4, 5, 6, 7]
def output_list(rlist):
    iter_list = iter(rlist)
    try:
        while True:
            print(next(iter_list))
    except StopIteration as e:
        print('Come to the end of the list!:', e)

output_list(test_list)

iter_list = iter(test_list)
for item in iter_list:
    print(item)

def factors(n):
    results = []
    for k in range(1, n+1):
        if n % k == 0:
            results.append(k)
    return results

print(factors(100))

def factors(n):
    for k in range(1, n+1):
        if n % k == 0:
            yield k

for ft in factors(100):
    print(ft)

n = 10
square = [k*k for k in range(1, n+1) if k in (1, 2, 3, 4, 5)]
print(square)