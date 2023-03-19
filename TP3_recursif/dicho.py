
import numpy as np

def dicho(liste,k):
    liste = np.sort(liste)
    if (len(liste)==1):
        if (liste[0]==k):
            return True
        else :
            return False
    else :
        if (liste[len(liste)//2]<k):
            return (dicho(liste[len(liste)//2+1:],k))
        elif (liste[len(liste)//2]>k):
            return (dicho(liste[:len(liste)//2],k))
        else :
            return True
        

test = [17,11,33,25,48,18,6]
t = dicho(test,60)
print(t)
        
