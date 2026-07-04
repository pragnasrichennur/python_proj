def mul_all(*args):
    prod = 1
    for i in args:
        prod *= i
    print(args)
    print(*args)
    return prod


print(mul_all(1,2,3,4,5))

