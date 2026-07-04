l=[1,2,3,4,5,6,7,8,9,10]
k=list(filter(lambda x:x%2==0,l))
m=list(map(lambda y:y*y,k))
print(m)
