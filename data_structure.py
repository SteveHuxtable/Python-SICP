class SequenceIterator:
    '''An iterator for any of Python's sequence types'''

    def __init__(self, sequence):
        self._seq = sequence
        self._k = -1

    def __next__(self):
        self._k += 1
        if self._k < len(self._seq):
            return(self._seq[self._k])
        else:
            raise StopIteration('come to the end of the seq') # whether the () exists is okay!

        def __iter__(self):
            return self

test_list = [1, 2, 3, 4, 5, 6, 7, 8]
test_list = SequenceIterator(test_list)

class Range:

    def __init__(self, start, stop=None, step=1):
        if step == 0:
            raise ValueError('step cannot be 0')
        if stop is None:
            start, stop = 0, start
        self._length = max(0, (stop - start + step - 1) // step) 
        self._start = start
        self._step = step

        def __len__(self):
            return self._length
        
        def __getitem__(self, k):
            if k < 0:
                k += len(self)
            
            if not 0 <= k < self._length:
                raise IndexError('index out of range')
            
            return self._start + k * self._step

class Progression:

    def __init__(self, start=0):
        self._current = start
    
    def _advance(self):
        self._current += 1
    
    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        return self

    def print_progression(self, n):
        print(' '.join(str(next(self) for j in range(n)))) # ???

import copy
test_list = [1, 2, 3, 4, 5, 6]
test_list_copy = copy.copy(test_list)
test_list_deepcopy = copy.deepcopy(test_list)

import copy
origin = [1, 2, [3, 4]]
#origin 里边有三个元素：1， 2，[3, 4]
cop1 = copy.copy(origin)
cop2 = copy.deepcopy(origin)
origin[2][0] = "hey!"