def log():
    ar1 = []
    with open("Paroli.txt","r") as f:
        r = f.read()
        ar = r.split()
    for i in range(0,len(ar)):
        a = ar[i].split("@")
        ar1.append(a)
    return ar1

def Afftar():
    auf = log()
    a = input("login:")
    b = input("password:")
    for i in range(0,len(auf),1):
        if a == auf[i][0] and b == auf[i][1]:
            print("Welcome")