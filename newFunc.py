# recursion: when a function calls itself we call it recursion
def show(n):
    print(n)
    if (n == 1):
        return     # stop
    show(n-1)

show(10)
