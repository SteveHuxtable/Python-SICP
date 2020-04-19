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