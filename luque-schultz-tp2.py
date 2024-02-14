# Mattéo LUQUE L3 CMI Informatique
# Paul SCHULTZ L3 Informatique groupe 1



from graphe import *


if __name__ == "main":
	noeuds = [Noeud("A"), Noeud("B"), Noeud("C"), Noeud("D"), Noeud("E"), Noeud("F"), Noeud("G")]


	main(8)


def evaporation(liens):
    for i in liens:
        i.pheromone = i.pheromone * 0.7


def passage(lien):
    lien.pheromone = lien.phermomone + (1 / lien.distance * Graphe.a) # TODO graphe a remettre en variable



