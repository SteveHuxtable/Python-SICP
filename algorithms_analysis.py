seq = [1, 2, 3, 4, 5, 6, 7]

def linear_sum(S, n):
    '''Return the sum of the first n numbers in a seq'''
    if n == 0:
        return 0
    else:
        return linear_sum(S, n-1) + S[n-1]

def reverse(S, start = 0, stop = 0):
    if stop == 0:
        stop = len(S) - 1
    if start < stop - 1:
        S[start], S[stop-1] = S[stop-1], S[start]
        reverse(S, start+1, stop-1)

def power(x, n):
    if n == 0:
        return 1
    else:
        partial = power(x, n // 2)
        result = partial * partial
        if n % 2 == 1:
            result *= x
        return result