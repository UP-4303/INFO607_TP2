from typing import List
from lien import Lien

class Noeud:
	label: str
	connexions: List[Lien]
	x:float
	y:float

	def __init__(self, label: str):
		self.label = label
		self.connexions = []
		self.x = 0
		self.y = 0

	def Connecte(self, other, distance: int = 1, maxPheromones: float = 10): # TODO type hint
		lien = Lien(self,other, distance, maxPheromones= maxPheromones)
		self.connexions.append(lien)
		other.connexions.append(lien)
		return lien

# Formate une liste de noeuds comme un chemin, en string
def strChemin(noeuds: List[Noeud]):
	string: str = noeuds[0].label
	for noeudIndex in range(1,len(noeuds)):
		string += "->"+noeuds[noeudIndex].label
	return string