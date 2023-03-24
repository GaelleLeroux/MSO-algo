
def TriRapide(liste):
    n = len(liste)
    if n<=1:
        return liste
    else:
        ind_piv = len(liste)-1
        pivot = liste[ind_piv]
        L = 0
        R = len(liste)-2
        while L!=R:
            while L!=ind_piv and liste[L]<pivot:
                L+=1
            if L!=ind_piv:
                while liste[R]>pivot and L!=R:
                    R-=1
                liste[R],liste[L] = liste[L],liste[R]
            else:
                break
        if L==R:
            liste[L],liste[ind_piv] = liste[ind_piv],liste[L]
            ind_piv = L
        if n==2:
            return liste
        else :
            l1 = TriRapide(liste[:ind_piv])
            l2 = TriRapide(liste[ind_piv+1:])
            l1.append(pivot)
            for i in range(len(l2)):
                l1.append(l2[i])
            return l1
    
    
    
        
liste = [3,5,8,1,2,9,4,7,6]
print(TriRapide(liste))


