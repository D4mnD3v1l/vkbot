def AddData(a):
    file = open('store.txt','a')
    file.write(a + '\n')
    file.close()
def Clear():
    file = open('store.txt','w')
    file.write("")
    file.close()
def ReadData():
    file = open('store.txt.','r')
    print(file.read())
    file.close()
ReadData()

