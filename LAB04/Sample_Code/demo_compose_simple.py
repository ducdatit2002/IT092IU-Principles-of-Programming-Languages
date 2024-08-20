from functools import reduce

def compose(*funcs):
    def h(*args):
        return reduce(lambda x, y: (y(*x),), reversed(funcs), args)[0]
    return h

def add1(x):
    return x + 1

def times2(x):
    return x * 2

def subtract3(x):
    return x - 3

composed_function = compose(add1, times2, subtract3)


result = composed_function(4)
print(result)  # Expected output: ((4 - 3) * 2) + 1 = 3
