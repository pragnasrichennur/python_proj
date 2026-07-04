d={"apple":100,"banana":40,"cherry":150}
# def great(x):
#     if x>50:
#         return x
# m=list(filter(great,d.values()))
# print(m)
k=list(filter(lambda x:x>50,d.values()))
print(k)
