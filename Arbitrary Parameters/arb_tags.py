def dis_tags(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
    print(kwargs)
    print(*kwargs)

dis_tags(size='M',rate='300',brand="Denim")
