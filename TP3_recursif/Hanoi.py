def Hanoi(n,D,A,I):
    if n!=0:
        Hanoi(n-1, D, I, A)
        print("Déplacer le disque de "+str(D)+ " vers " +str(A))
        Hanoi(n-1, I, A, D)

Hanoi(3,1,2,3)
        