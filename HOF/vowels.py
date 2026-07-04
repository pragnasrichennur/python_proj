l='Pragna'
# Without lambda
def vowel(x):
    return x not in "AEIOUaeiou"
k=list(filter(vowel,l))
print(k)

# With lambda
m=list(filter(lambda x: x not in "AEIOUaeiou",l))
print(m)