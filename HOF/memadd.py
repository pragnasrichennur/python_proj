l=[10,350,10,350,20]
k=list(map(lambda x:id(x),l))
print(k)

# the addresses are same coz both the values are same and they both stored at the same address
## Python reuses the same object for identical immutable values (such as integers, strings, and tuples) whenever possible. Since integers are immutable, multiple references to the same value can point to the same object in memory, resulting in repeated addresses.