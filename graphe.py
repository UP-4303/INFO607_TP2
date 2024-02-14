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

	# def __init__(self, noeuds: List[Noeud], liens: List[Lien], evaportation: float = 0.7, q: int = 1, a: float = 1., b: float = 1.):
	# 	self.noeuds = noeuds
	# 	self.liens = liens
	# 	self.evaporation =  evaportation
	# 	self.q = q
	# 	self.a = a
	# 	self.b = b

	def __init__(self, nbNoeuds: int, maxDistance: int, evaportation: float = 0.7, q: int = 1, a: float = 1., b: float = 1., maxPheromones: float = 10):
		self.noeuds = []
		self.liens = []
		self.evaporation =  evaportation
		self.q = q
		self.a = a
		self.b = b

		for i in range(nbNoeuds):
			noeud = Noeud(str(i))
			for otherNoeud in self.noeuds:
				self.liens.append(noeud.Connecte(otherNoeud, randint(1, maxDistance), maxPheromones))
			self.noeuds.append(noeud)

		for i in range(len(self.noeuds)):
			self.noeuds[i].x = 0
			self.noeuds[i].y = 0

	def __str__(self):
		return "test"

	def Evaporer(self):
		for lien in self.liens:
			lien.Evaporer(self.evaporation)

	def LancerFourmi(self, depart: Noeud):
		fourmi = Fourmi(self.noeuds.copy(), depart)
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