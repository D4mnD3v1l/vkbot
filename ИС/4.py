a = [ 1, -2, 3, -4, 0, 1, -2, 3, -4, 0, 3, 6, 44, -23]
null = 0
otric = 0
poloz = 0
for i in range (0,len(a),1):
    if a[i] == 0:
        null += 1
    elif a[i] > 0:
        poloz += 1
    elif a[i] < 0:
        otric += 1
print("0 =", null)
print("+ =", poloz)
print("- =", otric)