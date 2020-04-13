def iter_improve(update, test, guess = 1):
    while not test(guess):
        guess = update(guess)
    print("matched value: " + str(guess))
    return guess

def approx_eq(a, b, tolerance = 1e-5):
    return abs(a-b) < tolerance

def square(x):
    return (x * x)

def average(a, b):
    return (a + b) / 2

def sqrt(x):
    def update(guess):
        return average(guess, x/guess)
    def test(guess):
        return approx_eq(square(guess), x)
    guess = iter_improve(update, test, guess = 1)
    return guess

if __name__ == "__main__":
    print(sqrt(9))    