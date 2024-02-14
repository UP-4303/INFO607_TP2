from typing import Tuple

class Lien:
	noeuds: Tuple[any, any] # TODO type hint
	distance: int
	pheromone: float

	def __init__(self, noeud1, noeud2, distance = 1):
		self.noeuds = (noeud1, noeud2)
		self.distance = distance
		pheromone = 1.

	def Passage(self, a: float):
		self.pheromone += a / self.distance