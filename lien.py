from typing import Tuple

class Lien:
	noeuds: Tuple[any, any] # TODO type hint
	distance: int
	pheromone: float
	max: float
	min: float

	def __init__(self, noeud1, noeud2, distance = 1, maxPheromones = 10):
		self.noeuds = (noeud1, noeud2)
		self.distance = distance
		self.pheromone = 1.
		self.max = maxPheromones
		self.min = 1

	def Passage(self, a: float):
		self.pheromone = min(self.max, self.pheromone + (a / self.distance))

	def Evaporer(self, evaporation: float):
		self.pheromone = max(self.min, self.pheromone * (1 - evaporation))