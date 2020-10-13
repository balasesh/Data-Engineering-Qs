import random

def rand_function():
    print(random.randrange(1,10))
    x = 1 # int
    y = 2.8 # float
    z = 1j # complex

    #convert from int to float:
    a = float(x)
    b = int(y)
    print(a)
    print(b)

rand_function()