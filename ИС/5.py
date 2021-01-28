a = [[1,2,3,4],[1,2,66,3],[2,1,0,2],[1,1,1,1],[2,2,2,2]]
for i in range (0, len(a),1):
    for j in range (0,len(a[i]),1):
        a[i][j] = a[i][j]**2
print (a)