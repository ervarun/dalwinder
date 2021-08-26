# 0 1 1 2 3 5 8

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


n = int(input("Enter the value of n for fib series"))

if (n <= 0):
    print("Enter a positive number")
else:
    for i in range(n):
        print(fib(i))




