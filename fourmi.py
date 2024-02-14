from typing import List, Tuple
from graphe import *

class Fourmi :
	position : Noeud

	def __init__(self, position):
	    self.position = position

	def __str__(self):
		return f"Position :{self.position.label}"