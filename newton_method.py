def iter_improve(update, test, guess):
    while not test(guess):
        guess = update(guess)
    print(guess)
    return guess

def approx_eq(a, b, tolerance = 1e-5):
    return (a - b) < tolerance

def square(x):
    return (x * x)

def square_root(a):
    return find_root(lambda x: square(x) - a)

def find_root(f, initial_guess=10):
    def test(x):
        print(approx_eq(f(x), 0))
        return approx_eq(f(x), 0)
    return iter_improve(newton_update(f), test, initial_guess)

def approx_derivative(f, x, delta = 1e-5):
    df = f(x + delta) - f(x)
    return df/delta

def newton_update(f):
    def update(x):
        return x - f(x) / approx_derivative(f, x)
    print(update)
    return update


if __name__ == "__main__":
    print("Sqrt(16) is :")
    print(square_root(16))
    print("Sqrt(10) is :")
    print(square_root(10))