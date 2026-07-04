# Yes we can call another function inside a lambda function

def sq(n):
    return n*n
squ=lambda n:sq(n)+n
print(squ(5))


# The three main limitations of lambda functions compared to def functions are:
#
# 1. Only a single expression is allowed
# A lambda function can contain only one expression and cannot have multiple statements.
# 2. Cannot contain complex statements
# Statements such as if-else blocks (multi-line), for loops, while loops, try-except, and return statements cannot be used inside a lambda function.
# 3.Less readable and harder to maintain
# Lambda functions are best for short, simple operations. For complex logic, def functions are easier to read, debug, and maintain.