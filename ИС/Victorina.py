def Vict():
    file = open("q.txt","r")
    st = file.read()
    stt = st.split("\n")
    stt = st.split("@")
    
    print(stt)
Vict()