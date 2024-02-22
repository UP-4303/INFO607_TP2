from typing import Dict, List
from noeud import Noeud
from random import random
from lien import Lien

class Fourmi :
	position : Noeud
	aVoir: List[Noeud] # TODO Possibilité de passer plusieurs fois par ville, en fonction de q
	depart: Noeud
	chemin: List[Noeud]
	distanceParcourue: int
	liens: Dict[str, Dict[str, Lien]]

	def __init__(self, noeuds: List[Noeud], position: Noeud, liens:Dict[str, Dict[str, Lien]]):
		self.position = position
		self.aVoir = noeuds
		self.depart = position
		self.aVoir.remove(self.depart)
		self.chemin = []
		self.distanceParcourue = 0
		self.chemin.append(position)
		self.liens = liens

	def __str__(self):
		return f"Position :{self.position.label}"

	def __str__(self):
		return f"Position :{self.position.label}"

	def Avancer(self, a:float, b: float)-> bool: # La sortie indique si la fourmi a avancée
		pheromoneTotal = 0

		# Liens possibles
		liens: Dict[Noeud, Lien] = {}
		for noeud in self.aVoir:
			if(noeud.label < self.position.label):
				lien = self.liens[noeud.label][self.position.label]
			else:
				lien = self.liens[self.position.label][noeud.label]
			liens[noeud] = lien
			pheromoneTotal+=lien.pheromone
		
		if len(liens) == 0:
			return False

		# On choisit le lien vers l'un des noeuds restants
		lien: Lien
		rand: float = random()*pheromoneTotal
		pheromonePasse: float = 0.
		index: int = 0
		keys: List[str] = list(liens.keys())
		# "while True: if x: break" ou "Comment émuler une boucle 'do while' en python"
		while True:
			pheromonePasse += liens[keys[index]].pheromone
			if pheromonePasse >= rand:
				lien = liens[keys[index]]
				break
			index+=1

		# On applique le passage
		lien.Passage(a)
		self.position = keys[list(liens.values()).index(lien)]
		
		self.distanceParcourue += lien.distance
		self.aVoir.remove(self.position)
		self.chemin.append(self.position)

		# Il faut que la fourmi retourne à son point de départ
		# Il ne faut pas l'ajouter au début, sinon elle pourrait y retourner dès son deuxième mouvement
		if self.aVoir == [] and self.position != self.depart:
			self.aVoir.append(self.depart)
		
		return True

