from typing import List
from graphe import *
from random import random

class Fourmi :
    position : Noeud
    vus: List[Noeud] # TODO Possibilité de passer plusieurs fois par ville, en fonction de q

    def __init__(self, position):
        self.position = position
        self.vus.append(position)

    def Avancer(self, a:float, b: float)-> bool: # La sortie indique si la fourmi a avancée
        liens = self.position.connexions
        liensTries = []
        pheromoneTotal = 0

        # On retire les liens vers des noeuds déjà vus
        for lien in liens:
            if ((lien.noeuds[0] == self.position) and (lien.noeuds[1] not in self.vus)) or ((lien.noeuds[1] == self.position) and (lien.noeuds[0] not in self.vus)):
                liensTries.append(lien)
                pheromoneTotal += lien.pheromone

        if len(liensTries) == 0:
            return False

        # On choisit le lien vers l'un des noeuds restants
        lien: Lien
        rand: float = random()*pheromoneTotal
        pheromonePasse: float = 0.
        index: int = 0
        # "while True: if x: break" ou "Comment émuler une boucle 'do while' en python"
        while True:
            pheromonePasse += liensTries[index].pheromone
            if pheromonePasse >= rand:
                lien = liensTries[index]
                break
            index+=1
        
        # On applique le passage
        lien.Passage(a)
        if lien.noeuds[0] == self.position:
            self.position = lien.noeuds[1]
        else:
            self.position = lien.noeuds[0]
        
        return True