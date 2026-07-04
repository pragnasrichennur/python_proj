## Regular
lis=[28,35,40,18,9]
def fun(f):
    return f*(9/5)+32
res = list(map(fun,lis))
print(res)

## Using lambda
res = list(map(lambda f:f*(9/5)+32,lis))
print(res)
