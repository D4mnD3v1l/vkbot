def PoprosheSdelaiBukvoiOdnoi (a,b):
    EstIliNet = 0
    for i in range (0,len(a),1):
        if b == a[i]:
            EstIliNet += 1
    if EstIliNet > 0:
        return True
    else:
        return False
print(PoprosheSdelaiBukvoiOdnoi([1,2,3,5],5))