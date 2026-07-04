from functools import reduce
l=[5,10,15,20,25,30]
k=reduce(list(filter(list(map(lambda x:x*x,l),lambda y:y%5==0,l))))
m=list(map(lambda x:x*x,l))