def run_twice(func,val):
    return func(func(val))

def add_one(x):
    return x+1
res = run_twice(add_one,5)
print(res)
