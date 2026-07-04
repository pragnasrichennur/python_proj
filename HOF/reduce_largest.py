from functools import reduce
l=[25,32,45,19,55,21,36]
k=reduce(lambda x,y:x if x>y else y,l)
print(k)
