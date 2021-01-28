def foo(n):
    if n == 1:
        print(n)
    else:
        foo(n-1)
        print(n)
foo(5)