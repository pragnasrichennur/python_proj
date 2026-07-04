from functools import reduce
l=['cat','elephant','dog','rhinoceros']
#Function
def long(x,y):
    if x>y:
        return x
    return y
k=reduce(long,l)
print(k)
#Lambda function
m=reduce(lambda x,y:x if x>y else y,l)
print(m)
