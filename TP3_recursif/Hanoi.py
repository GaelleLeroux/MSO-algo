def Hanoi(n,D,A,I):
    if n!=0:
        Hanoi(n-1, D, I, A)
        print("Déplacer le disque de "+str(D)+ " vers " +str(A))
        Hanoi(n-1, I, A, D)

Hanoi(3,1,3,2) #nombre de disques utilisés, emplacement de départ,emplacement d'arrivée,emplacement intermédiaire.
  
print("Mon hanoi : ////////////////////////////////:")      
        
def Ha(n,D,A,I):
    if n==1 :
        print("Déplacer le disque de "+str(D)+ " vers " +str(A))
    else :
        Ha(n-1,D,I,A)
        Ha(1,D,A,I)
        Ha(n-1,I,A,D)
        
Ha(3,1,3,2) #nombre de disques utilisés, emplacement de départ,emplacement d'arrivée,emplacement intermédiaire.