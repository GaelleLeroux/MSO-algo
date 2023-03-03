

class Noeuds :
    def __init__(self,x) :
        self.valeur = x
        self.suivant = None
    

    



class ListeChainee :
    def __init__(self) :
        self.head = None
        self.taille = 0

    def inserer(self,valeur,k) :
        self.taille+=1
        if k == 0:
            if self.head == None :
                self.head = Noeuds(valeur)
            else :
                new = Noeuds(valeur)
                new.suivant = self.head
                self.head = new
        else :
            if self.head == None :
                self.head = Noeuds(valeur)
            else :
                tempo = self.head
                trouver = True
                for i in range(0,k) :
                    if tempo.suivant == None :
                        tempo.suivant = Noeuds(valeur)
                        trouver = False
                        break
                    else :
                        tempo = tempo.suivant
                if (trouver) :
                    new = Noeuds(valeur)
                    new.suivant = tempo.suivant
                    tempo.suivant = new

    def supprimer(self,k) :
        if self.head == None :
            return "Liste vide"
        elif self.head.suivant == None :
            self.head = None
            self.taille-=1
        elif k==0 :
            self.head = self.head.suivant
            self.taille-=1
        else :
            self.taille-=1
            tempo = self.head
            tempo2 = tempo.suivant
            trouver = True
            for i in range(0,k-1) :
                if tempo2.suivant == None :
                    tempo.suivant = None
                    trouver = False
                    break
                else :
                    tempo = tempo2
                    tempo2 = tempo.suivant
            if (trouver) :
                tempo.suivant = tempo2.suivant
                    
    def rechercher(self,valeur) :
        tempo = self.head
        if self.head == None :
            print("Liste vide")
        else :
            i = 0
            while (tempo.suivant != None) :
                if (tempo.valeur == valeur):
                    print("valeur trouvée à la position " + str(i))
                tempo = tempo.suivant
                i+=1
            if (tempo.valeur == valeur):
                    print("valeur trouvée à la position " + str(i))
    
    def QuelTaille(self) :
        return self.taille



    def afficher(self) :
        self.tempo = self.head
        if (self.tempo==None) :
            print("liste vide")
        else :
            print(self.tempo.valeur)
            while (self.tempo.suivant != None):
                self.tempo = self.tempo.suivant
                print(self.tempo.valeur)
        
    def estVide(self) :
        if self.head == None :
            print("La liste est vide")
        else :
            print("La liste n'est pas vide")



a = ListeChainee()
print("Test liste vide :")
a.afficher()
a.inserer(0,0)
a.inserer(1,1)
a.inserer(2,2)
a.inserer(3,3)
print("Test insertion")
a.afficher()
print("Test suppresion")
a.supprimer(4)
a.afficher()
print("Test recherche")
a.inserer(0,45)
a.afficher()
a.rechercher(0)
print("Test taille")
print(str(a.QuelTaille()))
print("test estVide")
a.estVide()


        

