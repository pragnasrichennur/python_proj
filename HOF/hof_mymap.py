l=[2,4,6,8,10]
def my_map(x):
    return x*x
for i in l:
    my_map(i)
    print(my_map(i))

k=list(map(lambda x:x*x,l))
print(k)



