def mixed(a,b,*args,**kwargs):
    print("a is:",a,"b is:",b,"pos args:",args,"kw args",*kwargs.items())

mixed("pragna","sri","rishi","ani",siblings="Yes",Yop=2,Study="IIITK")