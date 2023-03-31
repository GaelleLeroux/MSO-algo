class Noeuds :
    def __init__(self,x) :
        self.valeur = x
        self.gauche = None
        self.droite = None

class Arbre:
    def __init__(self) :
        self.root = None
        self.taille = 0
    
    def creer(self,val):
        s = Noeuds(val)
        self.root = s
                
    def insererDroite(self,val):
        self.root.droite = val
        
    def insererGauche(self,val):
        self.root.gauche = val
                


def creerArbre(l):
    if len(l)!=1:
        a = Arbre()
        a.creer(l[0])
        u = l[1]
        b = creerArbre(l[2:len(l)-3])
        a.insererDroite(b)
        
        
        b = creerArbre(l[2:])
        a.insererGauche(b)
            return(a)
    else :
        a = Arbre()
        a.creer(l[0])
        return a
    
a = creerArbre(["a","?","b","?","c",":","d",":","e"])
    
    