# Mattéo LUQUE L3 CMI Informatique
# Paul SCHULTZ L3 Informatique groupe 1

from graphe import *
from fourmi import *

if __name__ == "__main__":
	noeuds: List[Noeud] = [Noeud("A"), Noeud("B"), Noeud("C"), Noeud("D"), Noeud("E"), Noeud("F"), Noeud("G")]
	liens: List[Lien] = []
	liens.append(noeuds[0].Connecte(noeuds[1], 2))
	liens.append(noeuds[0].Connecte(noeuds[3], 4))

	liens.append(noeuds[1].Connecte(noeuds[2], 2))
	liens.append(noeuds[1].Connecte(noeuds[3], 1))
	liens.append(noeuds[1].Connecte(noeuds[4], 3))
	liens.append(noeuds[1].Connecte(noeuds[6], 4))

	liens.append(noeuds[2].Connecte(noeuds[4], 1))
	liens.append(noeuds[2].Connecte(noeuds[5], 3))

	liens.append(noeuds[3].Connecte(noeuds[4], 3))
	liens.append(noeuds[3].Connecte(noeuds[5], 4))
	liens.append(noeuds[3].Connecte(noeuds[6], 4))

	liens.append(noeuds[4].Connecte(noeuds[5], 1))
	liens.append(noeuds[4].Connecte(noeuds[6], 3))

	liens.append(noeuds[5].Connecte(noeuds[6], 1))

	# Chemin le plus court de A à G : A->B->C->E->F->G (distance : 7) ou A->B->E->F->G (distance : 7)
	# Chemin le plus court pour le voyageur de commerce en partant de A : A->B->D->G->F->E->C (distance : 10)

	graphe: Graphe = Graphe(noeuds, liens)

	fourmis: List[Fourmi] = []
	for i in range(len(noeuds)):
		fourmis.append(Fourmi(noeuds[i]))


#------------Affichage----------------

	print(noeuds[1])
	for i in liens:
		print(i)
