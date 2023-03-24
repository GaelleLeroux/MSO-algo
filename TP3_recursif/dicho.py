
import numpy as np

def dicho(liste,listeV,k):
    n = len(liste);
    if (n==1):
        if (liste[0]==k):
            return listeV.index(k)
        else :
            return -1
    else :
        if (liste[n//2]<k):
            return (dicho(liste[n//2+1:],listeV,k))
        elif (liste[n//2]>k):
            return (dicho(liste[:n//2],listeV,k))
        else :
            return listeV.index(k)
        

test = [17,11,33,25,48,18,6]
liste = np.sort(test)
t = dicho(liste,test,17)
print(t)
        
