def foo(a, b):
    if a<b:
        foo(a, b - 1)
        print (b)
    elif a > b:
        print (a)
        foo (a - 1, b)
    else:
        print(a)
a = int(input())
b = int(input())
foo(a,b)