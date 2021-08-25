def show():
    print("some data")

def add(x,y):
    c=x+y
    print(c)

def greater(x,y,z):
    if x > y and x > z:
        print("x is greater")
    elif y > x and y > z:
        print("y is greater")
    elif z > x and z > y:
        print("z is greater")

# add(10,20)

greater(2,15,100)
