from functools import reduce
inp=['P','y','t','h','o','n']
res=reduce(lambda x,y:x+y,inp)
print(res)