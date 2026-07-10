# def validation(func):
#     def inner(*args):
#         # print(args)
#         # l = []
#         # for i in args:
#         #     if isinstance(i,int):
#         #         l.append(i)
#         # l = tuple(l)
#
#         l = tuple(filter(lambda x: isinstance(x,int),args))
#         return func(*l)
#
#     return inner
#
# @validation
# def just(*args):
#     print(f"args: {args}")
#     return sum(args)
#
# # print(just(1,2,3,'66',[45],123,'78'))
#
# def password_validator(func):
#     def inner(psd:str):
#         sp = ['@','*','!','#','$','%','&','_','-','=','+','/']
#         if len(psd)>=8:
#             up = list(filter(lambda x: x.isupper(),psd))
#             sc = list(filter(lambda x:x in sp, psd))
#             dg = list(filter(lambda x: x.isdigit(),psd))
#
#             print(up,sc,dg,sep='\n')
#
#             if up and sc and dg:
#                 print("Strong Password")
#                 func(psd)
#             else:
#                 print("Weak Password")
#         else:
#             print("password must contain 8 characters")
#     return inner
#
# @password_validator
# def password(ps):
#     print(f"password {ps} is accepted")
# password("23456fghbnkH")
# password("765FHGDk#$")

#




# def registration(func):
#     def inner(us,psd,age):
#         sp = ['@', '*', '!', '#', '$', '%', '&', '_', '-', '=', '+', '/']
#         if age>=18:
#             if us not in register:
#                 print("Correct username")
#             else:
#                 print("Try other username , it is already taken.")
#             if len(psd) >= 8:
#                 up = list(filter(lambda x: x.isupper(), psd))
#                 sc = list(filter(lambda x: x in sp, psd))
#                 dg = list(filter(lambda x: x.isdigit(), psd))
#                 print(up, sc, dg, sep='\n')
#                 if up and sc and dg:
#                     print("Strong Password")
#                     func(us,psd,age)
#                 else:
#                     print("Weak Password")
#             else:
#                 print("password must contain 8 characters")
#         else:
#             print("Age is under 18.")
#     return inner
# @registration
#
# def register(*args):
#     print("Registration Successful")
#
# register("pragna123","andhra#1",19)
#

registered_users = []

def registration(func):
    def inner(username, password, age):
        sp = ['@', '*', '!', '#', '$', '%', '&', '_', '-', '=', '+', '/']

        if age < 18:
            print("Age should be 18 or above.")
            return

        if username in registered_users:
            print("Username already exists. Try another username.")
            return


        if len(password) < 8:
            print("Password must contain at least 8 characters.")
            return

        up = list(filter(lambda x: x.isupper(), password))
        sc = list(filter(lambda x: x in sp, password))
        dg = list(filter(lambda x: x.isdigit(), password))

        if up and dg and sc:
            registered_users.append(username)
            func(username, password, age)
        else:
            print("Weak Password")
    return inner

@registration
def register(username, password, age):
    print("Registration Successful")

register("pragna123", "Andhra#123", 20)
register("pragna123", "Abcd@123", 22)
register("sri456", "hello123", 21)
register("anu789", "Anu@123", 16)





