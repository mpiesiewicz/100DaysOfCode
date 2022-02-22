
def add(*args):
    return sum(args)


print(add(7, 6, 3))

def calculate(n, **kwargs):
    print(kwargs)



calculate(2, add=3, multiply=5)