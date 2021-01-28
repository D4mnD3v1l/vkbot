def Victorina():
    i = 0
    score = 0
    while i < 3:
        print("""1. Kto perviy tyanul Repku v skazke pro Repku
        =====================
        1) Dedka
        2) Babka
        3) Serafim
        """)
        a = int(input())
        if a == 1:
            
            i += 1
            score += 1
        else:
            i += 1
        print("""2. Skolko bilo u babusi gusei?
        =====================
        1) 4
        2) 2
        3) 3
        """)
        a = int(input())
        if a == 2:
            i += 1
            score += 1
        else:
            i += 1
        print("""3. Kakaya otsenka samaya visokaya?
        =====================
        1) 2
        2) 4
        3) 5
        """)
        a = int(input())
        if a == 3:
            i += 1
            score += 1
        else:
            i += 1
    print ("Tvoi s4et:",score)