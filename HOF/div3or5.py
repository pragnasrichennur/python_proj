nums=[12,15,7,18,20,21,25]
k=list(filter(lambda x:x if (x%3==0 or x%5==0) and x%15!=0 else False,nums))
print(k)
