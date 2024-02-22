from typing import List
from lien import Lien
import numpy as npy

class Noeud:
	label: str
	connexions: List[Lien]
	x:float
	y:float

	def __init__(self, label: str, index: int, nbPoint: int):
		self.label = label
		self.connexions = []
		self.coord(index, nbPoint)

	def Connecte(self, other, distance: int = 1, maxPheromones: float = 10): # TODO type hint
		lien = Lien(self,other, distance, maxPheromones= maxPheromones)
		self.connexions.append(lien)
		other.connexions.append(lien)
		return lien

	def coord(self, index: int, nbPoint: int):
		angleR = npy.radians((360 / nbPoint)*index)
		self.x = 2* npy.cos(angleR)
		self.y = 2* npy.sin(angleR)

# Formate une liste de noeuds comme un chemin, en string
def strChemin(noeuds: List[Noeud]):
	string: str = noeuds[0].label
	for noeudIndex in range(1,len(noeuds)):
		string += "->"+noeuds[noeudIndex].label
	return string
