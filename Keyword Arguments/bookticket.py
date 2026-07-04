## Error is pos args is placed after keyword args

#def clay(color,texture,brand):
#    return color,texture,brand

#print(clay(texture="soft",color="purple","salona"))

##SyntaxError: positional argument follows keyword argument



def book_tic(name,flight,city,hours):
    return name,flight,city,hours

print(book_tic(city="Mumbai",name="Alice",hours=2,flight="Delhi"))


