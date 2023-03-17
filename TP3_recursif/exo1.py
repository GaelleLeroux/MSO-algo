def croissant(n,depart):
    if depart==n:
        print (depart)
    else :
        print(depart)
        croissant(n,depart+1)
        
def decroissant(n):
    if n==0:
        print (0)
    else:
        print(n)
        decroissant(n-1)
    
print("test croissant :")
croissant(5,0)
print("test decroissant :")
decroissant(5)