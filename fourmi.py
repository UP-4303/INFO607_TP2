from typing import List
from noeud import Noeud
from random import random
from lien import Lien

class Fourmi :
	position : Noeud
	aVoir: List[Noeud] # TODO Possibilité de passer plusieurs fois par ville, en fonction de q
	depart: Noeud
	chemin: List[Noeud]

	def __init__(self, noeuds: List[Noeud], position: Noeud):
		self.position = position
		self.aVoir = noeuds
		self.depart = position
		self.chemin.append(position)

	def __str__(self):
		return f"Position :{self.position.label}"

	def __str__(self):
		return f"Position :{self.position.label}"

	def Avancer(self, a:float, b: float)-> bool: # La sortie indique si la fourmi a avancée
		liens = self.position.connexions
		liensTries = []
		pheromoneTotal = 0

		# On retire les liens vers des noeuds déjà vus
		for lien in liens:
			if ((lien.noeuds[0] == self.position) and (lien.noeuds[1] in self.aVoir)) or ((lien.noeuds[1] == self.position) and (lien.noeuds[0] in self.aVoir)):
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
		
		self.aVoir.remove(self.position)
		self.chemin.append(self.position)
		
		return True

