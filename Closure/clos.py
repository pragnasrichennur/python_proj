def mul(x):
    def inner(y):
        return x*y
    return inner
k=mul(25)
l=mul(70)
print(k(30))
print(l(20))