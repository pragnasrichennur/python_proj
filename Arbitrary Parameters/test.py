def f(*args):
    print(type(args))

f(1,2,3)

## The output is tuple because they are positional args and pos args are stored in tuple format