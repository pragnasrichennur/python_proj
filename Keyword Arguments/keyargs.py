## Keyword arguments are more readable bcoz we enter the args along with the parameter name, so that we cannot be confused anymore

def cric(name,runs,wic,win):
    return name,runs,wic,win

print(cric(name="GT",runs=400,wic=9,win=1))

# It is easy to write keyword args as we will get to know which args we have passed till now
