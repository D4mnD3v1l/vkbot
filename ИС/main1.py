import libs.helpers as h
a = 1
while a == 1:
    print("Select: Add, Clear, Read or Exit")
    b = input()
    if b == "Add":
        h.AddData(input("Enter Data"))
    elif b == "Clear":
        h.Clear()
    elif b == "Read":
        h.ReadData()
    elif b == "Exit":
        a -= 1