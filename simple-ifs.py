# define a few variables
a = 10
b = 20
c = 30

# define a shorter print function
def p(p):
    print(p)

# define a simple function with if statements
def f(string):
    if string == a:
        p('10 potatoes 1')
    elif string == b:
        print('20 apples 2')
    elif string == c:
        print('30 grapes 3')
    else:
        print("NO MATCH")
        print(string)

# input string and use function
howdy=int(input("enter number"))
f(howdy)


