def SrednMass(a):
    summ = 0
    poloz = 0
    for i in range(0,len(a),1):
        if a[i] > 0:
            summ += a[i]
            poloz += 1
    b = summ / poloz
    print(b)
SrednMass([2,3,5,-1,3])