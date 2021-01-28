import random
m = int(input())
n = int(input())
a = []
while len(a) < m:
    a.append([])
for i in range (0, len(a),1):
        while len(a[i]) < n:
            a[i].append(random.randint(-10,10))
print(a)