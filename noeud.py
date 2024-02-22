from typing import List
from lien import Lien
import numpy as npy

class Noeud:
	label: str
	x:float
	y:float

	def __init__(self, label: str, index: int, nbPoint: int):
		self.label = label
		self.coord(index, nbPoint)

	def coord(self, index: int, nbPoint: int):
		angleR = npy.radians((360 / nbPoint)*index)
		self.x = npy.cos(angleR)
		self.y = npy.sin(angleR)

# Formate une liste de noeuds comme un chemin, en string
def strChemin(noeuds: List[Noeud]):
	string: str = noeuds[0].label
	for noeudIndex in range(1,len(noeuds)):
		string += "->"+noeuds[noeudIndex].label
	return string
