def multiplies(x):
    def inner(y):
        return x*y
    return inner

triple = multiplies(3)
print(triple(20))

