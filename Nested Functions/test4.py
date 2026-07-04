def fun():
    x=700
    def fun2():
        nonlocal x
        x=200;y=300
        print(x,y)
    print(x)
    fun2()
    print(x)
fun()


