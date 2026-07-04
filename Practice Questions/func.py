def func():
    name = input("What is your name: ")
    age = int(input("What is your age: "))
    branch = input("What is your branch: ")
    print("Name of the Person is: ",name)
    print("Age of the Person is: ", age)
    print("Branch of the Person is: ", branch, "\n")


while True:
    opinion = input("Type Yes or No :")
    if opinion == "Yes":
        func()
    else:
        print("Invalid")

