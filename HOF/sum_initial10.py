from functools import reduce
nums=[1,2,3,4]
k=reduce(lambda x,y:x+y,nums,10)
print(k)

## The initial values affects the reduction process,if we pass empty list then it will just return initial value rather than printing error

