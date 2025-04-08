import random as rd
import matplotlib.pyplot as plt
import numpy as np

def aleatoire(L):
    return rd.randint(0.1,2*np.sqrt(2)*L)
def distances(n,L):
    D=np.array([[0 for i in range(n)] for i in range(n)])
    for i in range(n):
        for j in range(i,n):
            if i!=j: 
                D[i][j]=aleatoire(L)               
    for i in range(n):
        for j in range(0,i):
            D[i][j]=D[j][i] 
    return D
    
    
# Solution n°1: Brute Force
# Objectif 1 : générer toute les permutations possible d'une liste à n nombre
def permutation(liste,resultat):
        if len(liste)==1:
            return [liste]
        for i in range(len(liste)):
            element=liste[i]
            reste=reste = liste[:i] + liste[i+1:]
            sous_permutation=permutation(reste,resultat)
            a=[element] + sous_permutation
            resultat.append(a)
        return resultat

#objectif 2 : calculer la distance totale pour chaque itinéraire possible et déterminer la distance minimale
def chemin_opti(n,L):
    resultat=permutation([i for i in range(1,n+1)])
    les_distances=distances(n,L)
    distance_min=[les_distances[1][2]]
    for i in resultat:
        distance_total=0
        for k in range(1,n):
            distance_totale=distance_totale + les_distances[k][k-1]
        if distance_totale < distance_min:
            distance_min=distance_totale
            chemin=i
    print("le chemin le plus optimisé est",i,"pour une distance parcourue de",distance_min)
    return chemin,distance_min

#Solution n°2: appliquer l'algorithme de ... pour rendre la tache moins couteuse
class arbre():
    def __init__(self, val ):
        self.gauche= None
        self.droite= None
        self.data= None
        
        