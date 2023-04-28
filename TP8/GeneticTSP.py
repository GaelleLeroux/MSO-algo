import os
import random as r
import csv
import GeneticTSPGui as g
import numpy as np
import copy

class Ville():
    def __init__(self,x,y,n) :
        self.x = x
        self.y = y
        self.nom = n

    def distance_vers(self,Ville):
        return ((self.x-Ville.x)**2+(self.y-Ville.y)**2)
    
    def __str__(self):
        return self.nom

    
def generer_ville(nb_villes=20):
    renvoie = []
    for i in range(nb_villes):
        renvoie.append(Ville(r.randint(0,300),r.randint(0,300),str(i)))
    return renvoie
    
def lire_csv(nom = "TP8/30.csv"):
    renvoie = []
    with open(nom, 'r') as f:
    # Créer un objet csv à partir du fichier
        obj = csv.reader(f)

        for ligne in obj:
            renvoie.append(Ville(int(ligne[1]),int(ligne[2]),ligne[0]))
    return renvoie

class Trajet:
    def __init__(self,liste=[]) :
        self.villes = liste
        self.parcours = liste
        self.longueur = 0
        #print(len(self.villes))
        if (len(self.villes)==0):
            self.longueur = 0
        else :
            r.shuffle(self.parcours)
            for i in range(len(self.parcours)-1):
                self.longueur = self.longueur + self.parcours[i].distance_vers(self.parcours[i+1])

    def calc_longueur(self):
        for i in range(len(self.parcours)-1):
            self.longueur = self.longueur + self.parcours[i].distance_vers(self.parcours[i+1])
        return
    
    def est_valide(self):
        for i in range(self.parcours):
            nmb = 0
            for j in range(self.parcours):
                if (self.parcours[j]==self.parcours[i]):
                    nmb+=1
                if (nmb>1):
                    return False
        return True


    def __str__(self):
        for i in range(len(self.parcours)):
            print(self.parcours[i])
        return ""

class Population:
    def __init__(self):
        self.liste_trajet = []

    def initialiser(self,taille,villes):
        for i in range(taille):
            self.liste_trajet.append(Trajet(villes))
        return
    
    def ajouter(self,trajet):
        self.liste_trajet.append(trajet)

    def meilleur(self):
        meilleur = sorted(self.liste_trajet, key= lambda Trajet : Trajet.longueur)
        return meilleur[0]
    
    def __str__(self):
        for i in range(len(self.liste_trajet)):
            print(self.liste_trajet[i])
        return ""

class PVC_Genetique:
    def __init__(self,l,t=40,genera=300,elistisme=True,mut_proba=0.3):
        self.GUI = g.PVC_Genetique_GUI(l)
        self.elit = elistisme
        self.proba = mut_proba
        self.liste = l
        self.taille_population = t
        self.generation = genera

    def croiser(self,parent1,parent2):
        enfant = Trajet()
        i = 0
        j = 0
        while len(enfant.parcours)!=len(parent1.parcours):
            if(i>j):
                if(parent1.parcours[i] in enfant.parcours):
                    i+=1
                else:
                    enfant.parcours.append(parent1.parcours[i])
            else:
                if(parent2.parcours[j] in enfant.parcours):
                    j+=1
                else:
                    enfant.parcours.append(parent2.parcours[j])

        enfant.calc_longueur()
        return enfant
    

    def muter(self,trajet):
        u = r.randint(0,len(trajet.villes)-1)
        v = r.randint(0,len(trajet.villes)-1)
        trajet.parcours[u],trajet.parcours[v] = trajet.parcours[v],trajet.parcours[u]
        trajet.calc_longueur()
        return

    def selectionner(self,population):
        p = Population()
        p.ajouter(population.meilleur())
        for i in range(int(len(population.liste_trajet)/2)):
            del population.liste_trajet[population.liste_trajet.index(population.meilleur())]
            p.ajouter(population.meilleur())

        if (len(p.liste_trajet)%2!=0):
            del population.liste_trajet[population.liste_trajet.index(population.meilleur())]
            p.ajouter(population.meilleur())

        return p

    def evoluer(self,population):
        select = self.selectionner(copy.copy(population))
        p = Population()
        if self.elit :
            for i in range(0, len(select.liste_trajet), 1):
                p.ajouter(select.liste_trajet[i])
            for i in range(0, len(select.liste_trajet), 2):
                p.ajouter(self.croiser(select.liste_trajet[i],select.liste_trajet[i+1]))

        else :
            for i in range(0, len(select.liste_trajet), 1):
                if r.random()<self.proba:
                    self.muter(select.liste_trajet[i])     

            for i in range(0, len(select.liste_trajet), 2):
                p.ajouter(self.croiser(select.liste_trajet[i],select.liste_trajet[i+1]))

        return p
    
    def executer(self):
        popula = Population()
        popula.initialiser(10,self.liste)
        best = copy.copy(popula.meilleur())
        afficher = True
        for i in range(self.generation):
             #self.clear_term()
             popula = self.evoluer(copy.copy(popula))
             tempo = copy.copy(popula.meilleur())
             print("tempo" + str(tempo.longueur))
             print("best " + str(best.longueur))
             if (tempo.longueur<best.longueur):
                 best = tempo
             if (i%5==0):
                 self.GUI.afficher(best,tempo,True)
        self.GUI.window.mainloop()
        return   


    def clear_term(self):
        os.system('cls' if os.name=='nt' else 'clear')

def main():
    a = lire_csv()
    #print(a)
    PVC = PVC_Genetique(a,False)
    PVC.executer()

    return

if __name__ == "__main__":
    main()