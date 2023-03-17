def maxliste(liste):
    if(len(liste)==2):
        if(liste[0]>=liste[1]):
            return(liste[0])
        else:
            return(liste[1])
    elif (len(liste)==1):
        return(liste[0])
    
    else:
        a = maxliste(liste[:len(liste)//2])
        b = maxliste(liste[len(liste)//2:])
        if (a>=b):
            return a
        else:
            return b
        
test = [17,11,33,25,48,18,6]
ma = maxliste(test)
print(ma)