import random
def D6(a):
    print("Vam vipalo:")
    print(a)
    c = random.randint(1,6)
    print("Soperniku vipalo:")
    print(c)
    if 6 > a > c:
        print("Win")
    elif a == c:
        print("Draw")
    elif a < c:
        print("Lose")
    elif a > 6:
        print("ERROR")
def D4(a):
    print("Vam vipalo:")
    print(a)
    c = random.randint(1,4)
    print("Soperniku vipalo:")
    print(c)
    if 4 > a > c:
        print("Win")
    elif a == c:
        print("Draw")
    elif a < c:
        print("Lose")
    elif a > 4:
        print("ERROR")
def D20(a):
    print("Vam vipalo:")
    print(a)
    c = random.randint(1,20)
    print("Soperniku vipalo:")
    print(c)
    if 20 > a > c:
        print("Win")
    elif a == c:
        print("Draw")
    elif a < c:
        print("Lose")
    elif a > 20:
        print("ERROR")
def D12(a):
    print("Vam vipalo:")
    print(a)
    c = random.randint(1,12)
    print("Soperniku vipalo:")
    print(c)
    if 12 > a > c:
        print("Win")
    elif a == c:
        print("Draw")
    elif a < c:
        print("Lose")
    elif a > 12:
        print("ERROR")