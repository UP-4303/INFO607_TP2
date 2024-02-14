from typing import List
from lien import Lien

class Noeud:
	label: str
	connexions: List[Lien]

	def __init__(self, label: str):
		self.label = label

	def Connecte(self, other, distance: int = 1): # TODO type hint
		lien = Lien(self,other, distance)
		self.connexions.append(lien)
		other.connexions.append(lien)
		return lien

# Formate une liste de noeuds comme un chemin, en string
def strChemin(noeuds: List[Noeud]):
	string: str = noeuds[0].label
	for noeudIndex in range(1,len(noeuds)):
		string += "->"+noeuds[noeudIndex].label
	return string