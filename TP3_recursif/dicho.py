
import numpy as np

def dicho(liste,listeV,k):
    liste = np.sort(liste)
    if (len(liste)==1):
        if (liste[0]==k):
            return listeV.index(k)
        else :
            return -1
    else :
        if (liste[len(liste)//2]<k):
            return (dicho(liste[len(liste)//2+1:],listeV,k))
        elif (liste[len(liste)//2]>k):
            return (dicho(liste[:len(liste)//2],listeV,k))
        else :
            return listeV.index(k)
        

test = [17,11,33,25,48,18,6]
t = dicho(test,test,18)
print(t)
        
