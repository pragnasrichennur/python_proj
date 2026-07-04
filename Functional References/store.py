def upper(x):
    return x.upper()
def lower(y):
    return y.lower()
def title(z,w):
    return z.concat(w)

oper={'upper':upper,'lower':lower,'string':title}

op = input("Enter your option:")
print(oper[op]("Apple"))
