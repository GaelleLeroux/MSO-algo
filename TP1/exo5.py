

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
            self.taille-=1
            tempo = self.fin.suivant
            for i in range(self.taille):
                self.fin = self.fin.suivant
            self.fin.suivant = tempo
        else :
            self.taille-=1
            tempo = self.fin
            tempo2 = tempo.suivant
            trouver = True
            for i in range(0,k) :
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
            print("La premier nombre de la liste est considéré comme étant à la ligne 1 : ")
            tempo = self.fin.suivant
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

    def creaction_cercle(self,nombre) :
        while (nombre!=0):
            self.inserer(nombre,0)
            nombre-=1
            
    def survivant(self,numero):
        if self.fin == None :
            return "Liste vide, pas de cercle existant"
        else :
            tempo = self.fin.suivant
            for i in range(0,numero-1) :
                tempo = tempo.suivant
            replique = self.taille
            while(replique != 1):
                for i in range(3):
                    tempo = tempo.suivant
                    while(tempo.valeur==None):
                        tempo = tempo.suivant
                tempo.valeur = None
                replique-=1
            tempo = tempo.suivant
            while(tempo.valeur==None):
                tempo = tempo.suivant
            print("Le dernier survivant est : " + str(tempo.valeur))

    def survivant2(self,numero):
        if self.fin == None :
            return "Liste vide, pas de cercle existant"
        else :
            while(self.taille != 1):
                for i in range(2):
                    numero+=1
                self.supprimer((numero)%50)
            print("Le dernier survivant est : " + str(self.fin.valeur))



a = ListeChainee()
print("Test creation cercle")
a.creaction_cercle(50)
a.supprimer(5)
a.afficher()
print("Test survivant")
a.survivant(46)

b = ListeChainee()
b.creaction_cercle(50)
print("Test survivant2222222222222222")
b.survivant2(46)
b.afficher()


        

