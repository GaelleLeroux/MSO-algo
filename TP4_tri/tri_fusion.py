
def TriFusion(liste):
    n = len(liste)
    if n==1:
        return liste
    elif n==2:
        if liste[0]>liste[1]:
            liste[0],liste[1] = liste[1],liste[0]
            return liste
        else:
            return liste
    else :
        liste1 = TriFusion(liste[n//2:])
        liste2 = TriFusion(liste[:n//2])
        listeF = []
        n1 = len(liste1)
        n2 = len(liste2)
        i = 0;
        j = 0;
        while i!=n1 and j!=n2:
            u = liste1[i]
            v = liste2[j]
            if u>v:
                listeF.append(v)
                j+=1
            else:
                listeF.append(u)
                i+=1
        if i!=n1:
            for i in range(i,n1):
                listeF.append(liste1[i])
        if j!=n2:
            for j in range(j,n2):
                listeF.append(liste2[j])
        return listeF
 
 
       

a = [17,11,33,25,18,6]

print(TriFusion(a))