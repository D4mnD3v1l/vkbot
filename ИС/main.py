import random
import GameFunc.Dice as D
import GameFunc.Mass as M
import GameFunc.Vict as V
import GameFunc.Credits as C
print("Select Function")
print("""===========
1.Dices
2.Massive
3.Victorina
4.Credits
===========""")
j = int(input())
if j == 1:
    print("Select Dice")
    k = input()
    if k == "D4":
        D.D4(random.randint(1,4))
    elif k == "D6":
        D.D6(random.randint(1,6))
    elif k == "D12":
        D.D12(random.randint(1,12))
    elif k =="D20":
        D.D20(random.randint(1,20))   
elif j == 2:
    print("Vvedite kolichestvo elementov massiva")
    M.Massive(int(input()))
elif j == 3:
    V.Victorina()
elif j == 4:
    C.Credits()