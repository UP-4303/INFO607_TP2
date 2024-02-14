from typing import List, Tuple

class Lien:
	noeuds: Tuple[any, any] # TODO type hint
	distance: int
	pheromone: float

	def __init__(self, noeud1, noeud2, distance = 1):
		self.noeuds = (noeud1, noeud2)
		self.distance = distance
		pheromone = 0.

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