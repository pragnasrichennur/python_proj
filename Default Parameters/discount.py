def dis_price(price,dis=10):
    return price*(dis/100)

if __name__ == "__main__":
    print(dis_price(400,20))#with discount arg
    print(dis_price(300,))#without discount arg


## 5. Using def param makes a function more flexible and reusable instead of fixing value inside the function
def test(name,msg="Hello"):
    return msg,name

if __name__ == "__main__":
    print(test("Alice"))