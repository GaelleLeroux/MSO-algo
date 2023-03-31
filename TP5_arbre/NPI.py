
def cal(u,nmb1,nmb2)  :
    if (u=="+"):
        nmb1 = nmb1 + nmb2
    if (u=="/"):
        nmb1 = nmb1 / nmb2
    if (u=="*"):
        nmb1 = nmb1 * nmb2
    if (u=="**"):
        nmb1 = nmb1 ** nmb2
    return nmb1
      
def NPI(s):
    l = s.split()
    operateur = ["+","/","*","**"]
    nmb = []
    for i in range(0,len(l)):
        u = l[i]
        if u in operateur:
            nmb1 = nmb.pop()
            nmb2 = nmb.pop()
            nmb.append(cal(u,nmb1,nmb2))
                
        else :
            nmb.append(int(u))
    print(nmb[0])
    
        
NPI("2 3 * 4 5 * +")        