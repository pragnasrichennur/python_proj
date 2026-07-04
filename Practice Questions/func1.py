def tree(monkey_count,fruit_type,fruit_count):

    dict = {"mango": 2, "Apple": 3, "Orange": 1.5}
    t = dict[fruit_type.lower()]
    x = int(fruit_count/monkey_count)
    tt = t*x
    print("Time taken to complete the fruits by total monkeys is :",tt)

tree(monkey_count = 5,fruit_count = 20,fruit_type = "Mango")

# To change the float numbers to integer
#if instance(x,float):
#    x=int(x)+1
#    tt = t*x
