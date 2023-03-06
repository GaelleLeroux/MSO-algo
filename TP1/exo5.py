

class Noeuds :
    def __init__(self,x) :
        self.valeur = x
        self.suivant = None
    

    



class ListeChainee :
    def __init__(self) :
        self.fin = None
        self.taille = 0

    def inserer(self,valeur,k) :
        self.taille+=1
        if k == 0:
            if self.fin == None :
                self.fin = Noeuds(valeur)
                self.fin.suivant = self.fin
            else :
                new = Noeuds(valeur)
                new.suivant = self.fin.suivant
                self.fin.suivant = new
        elif k>=self.taille-1 :
            new = Noeuds(valeur)
            new.suivant = self.fin.suivant
            self.fin.suivant = new
            self.fin = new
        else :
            if self.fin == None :
                self.fin = Noeuds(valeur)
            else :
                tempo = self.fin.suivant
                trouver = True
                for i in range(1,k) :
                    tempo = tempo.suivant
                if (trouver) :
                    new = Noeuds(valeur)
                    new.suivant = tempo.suivant
                    tempo.suivant = new

    def supprimer(self,k) :
        if self.fin == None :
            return "Liste vide"
        elif self.fin.suivant == None :
            self.fin = None
            self.taille-=1
        elif k==0 :
            tempo = self.fin.suivant
            self.fin.suivant = tempo.suivant
            self.taille-=1
        elif k>=self.taille :
            tempo = self.fin.suivant
            for i in range(self.taille-1):
                self.fin = self.fin.suivant
            self.fin.suivant = tempo
        else :
            self.taille-=1
            tempo = self.fin
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
        tempo = self.fin
        if self.fin == None :
            print("Liste vide")
        else :
            i = 1
            while (i<self.taille) :
                if (tempo.valeur == valeur):
                    print("valeur trouvée à la position " + str(i))
                tempo = tempo.suivant
                i+=1
            if (tempo.valeur == valeur):
                    print("valeur trouvée à la position " + str(i))
    
    def QuelTaille(self) :
        return self.taille



    def afficher(self) :
        tempo = self.fin
        if (tempo==None) :
            print("liste vide")
        else :
            tempo = tempo.suivant
            print(tempo.valeur)
            i = 0
            while (i<self.taille-1):
                i+=1
                tempo = tempo.suivant
                print(tempo.valeur)
        
    def estVide(self) :
        if self.fin == None :
            return True
        else :
            return False





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

        

