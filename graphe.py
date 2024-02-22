from typing import Dict, List
from fourmi import Fourmi
from random import randint
from lien import Lien
from noeud import Noeud, strChemin
import matplotlib.pyplot as plt

class Graphe:
	noeuds: List[Noeud]
	liens: List[Lien]
	evaporation: float
	q: int # Nombre de fois que les noeuds doivent être visités
	a: float # Quantité de pheromones laissé sur un lien (à diviser par la distance)
	b: float # Importance des pheromones

	# def __init__(self, noeuds: List[Noeud], liens: List[Lien], evaportation: float = 0.7, q: int = 1, a: float = 1., b: float = 1.):
	# 	self.noeuds = noeuds
	# 	self.liens = liens
	# 	self.evaporation =  evaportation
	# 	self.q = q
	# 	self.a = a
	# 	self.b = b

	def __init__(self, nbNoeuds: int, maxDistance: int, evaportation: float = 0.7, q: int = 1, a: float = 1., b: float = 1., maxPheromones: float = 10):
		self.noeuds = []
		self.liens: Dict[str, Dict[str, Lien]] = {}
		self.evaporation =  evaportation
		self.q = q # 
		self.a = a # Quantité de phéromones déposée à chaque passage
		self.b = b #

		for i in range(nbNoeuds):
			self.noeuds.append(Noeud(str(i), i, nbNoeuds))
		self.noeuds.sort(key=(lambda noeud: noeud.label))

		for i in range(0, len(self.noeuds)-1):
			self.liens[self.noeuds[i].label] = {}
			for j in range(i+1, len(self.noeuds)):
				self.liens[self.noeuds[i].label][self.noeuds[j].label] = Lien(randint(1, maxDistance), maxPheromones)

		plt.xlim(-5, 5)
		plt.ylim(-5, 5)
		plt.gca().set_aspect('equal', adjustable='box')
		plt.scatter([noeud.x for noeud in self.noeuds], [noeud.y for noeud in self.noeuds])
		for i in range(0, len(self.noeuds)-1):
			for j in range(i+1, len(self.noeuds)):
				plt.plot([self.noeuds[i].x, self.noeuds[j].x], [self.noeuds[i].y, self.noeuds[j].y], '-', linewidth=(1))
		plt.show()

	def __str__(self):
		return "test"

	def Evaporer(self):
		for i in range(0, len(self.noeuds)-1):
			for j in range(i+1, len(self.noeuds)):
				self.liens[self.noeuds[i].label][self.noeuds[j].label].Evaporer(self.evaporation)

	def LancerFourmi(self, depart: Noeud):
		fourmi = Fourmi(self.noeuds.copy(), depart, self.liens)
		while(True):
			if not fourmi.Avancer(self.a, self.b):
				break
		if(len(fourmi.aVoir) == 0):
			print(f"Chemin trouvé : {strChemin(fourmi.chemin)} avec une distance de {fourmi.distanceParcourue}")

	def LancerFourmisAleatoirement(self, iterations: int):
		for i in range(iterations):
			self.LancerFourmi(self.noeuds[randint(0,len(self.noeuds)-1)])
			self.Evaporer()

	def LancerFourmis(self, depart: Noeud, iterations: int):
		for i in range(iterations):
			self.LancerFourmi(depart)
			self.Evaporer()