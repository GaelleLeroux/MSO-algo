
def Syracus(n,liste):
    liste.append(n)
    if n==1:
        return (liste,len(liste),max(liste))
        
    elif n%2==0:
        return(Syracus(n/2,liste))
        
    else :
        return(Syracus(3*n+1,liste))
        



[liste,vol,max2] = Syracus(28,[])
print(liste)
print(vol)
print(max2)

