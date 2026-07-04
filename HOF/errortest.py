from functools import reduce

l=[3,5,9,14,18]
# If exactly one parameter is used
k=reduce(lambda x:x+3,l)
print(k)
#Output: TypeError: <lambda>() takes 1 positional argument but 2 were given


# If exactly three parameters is used
m=reduce(lambda x,y,z:x+y+z,l)
print(m)
#Output: TypeError: <lambda>() missing 1 required positional argument: 'z'
