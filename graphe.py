from typing import List
from fourmi import Fourmi
from random import randint
from lien import Lien
from noeud import Noeud, strChemin

class Graphe:
	noeuds: List[Noeud]
	liens: List[Lien]
	evaporation: float
	q: int # Nombre de fois que les noeuds doivent être visités
	a: float # Quantité de pheromones laissé sur un lien (à diviser par la distance)
	b: float # Importance des pheromones

	def __init__(self, noeuds: List[Noeud], liens: List[Lien], evaportation: float = 0.7, q: int = 1, a: float = 1., b: float = 1.):
		self.noeuds = noeuds
		self.liens = liens
		self.evaporation =  evaportation
		self.q = q
		self.a = a
		self.b = b

	def Evaporer(self):
		for lien in self.liens:
			lien.pheromone *= 1-self.evaporation

	def LancerFourmi(self, depart: Noeud):
		fourmi = Fourmi(depart)
		while(True):
			if not fourmi.Avancer(self.a, self.b):
				break
		if(len(fourmi.aVoir) == 0):
			print(f"Chemin trouvé : {strChemin(fourmi.chemin)}")

	def LancerFourmis(self, iterations: int):
		for i in range(iterations):
			self.LancerFourmi(self.noeuds[randint(0,len(self.noeuds-1))])
			self.Evaporer()