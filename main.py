
from operator import index


class GrapheOriente():


    def __init__(self, graph = {}) -> None:
        if graph == {}:
            self.graph = {}
        else:
            self.graph = graph

    def get_dico(self):
        return self.graph

    def ajouter_sommet(self, sommet):
        self.graph[sommet] = [] 
    
    def supprimer_sommet(self, sommet):
        try:
            del self.graph[sommet]
        except:
            print("Sommet introuvable, merci de vérifier l'ortographe")

    def ajouter_arc(self, s1, s2):
        try: 
            new = [self.graph[s1]][0]
            new.append(s2)
            self.graph[s1] = new 
        except:
            print('Un des deux sommets spécifiés ne semble pas exister !')

    def supprimer_arc(self,s1,s2):
        try:
            new = [self.graph[s1]][0]
            del new[new.index(s2)]
        except:
           print('Un des deux sommets spécifiés ne semble pas exister !')

    def sommets(self):
        sommets = []
        for i in self.graph.keys():
            sommets.append(i)
        return sommets

    def nb_sommets(self):
        return len(self.sommets())

    def nb_arcs(self):
        cpt = 0 
        for i in self.graph.keys():
            cpt += len(self.graph[i])
        return cpt 

    def successeurs(self, sommet):
        return self.graph[sommet]

    def predecesseurs(self, sommet):
        l = []
        for v in self.graph.keys():
            if sommet in self.graph[v]:
                l.append(v)
        return l 

    def matrice(self):
        sommets = self.sommets()
        matrice = [] 
        for key in self.graph:
            tab = []
            prov = self.graph[key]
            for i in range(len(sommets)):
                if sommets[i] in prov:
                    tab.append(1)
                else:
                    tab.append(0)
            matrice.append(tab)
        return matrice
    
    def genereSommets(self, nb=10):
        """Cette méthode écrase des sommets si ils sont déjà existants !"""
        alpha = "abcdefghijklmnopqrstuvwxyz"
        if nb > 26: nb = 26 
        for i in range(nb):
            self.ajouter_sommet(alpha[i].upper())

    def __str__(self) -> str:
        mess = 'digraph G {\n'
        if self.graph == {}:
            return "Le Graph Oriente ne contient aucun sommet !"
        for i in self.graph.keys():
            for k in range(len(self.graph[i])):
                mess += f"\"{i}\" -> \"{self.graph[i][k]}\"\n"
        mess += '}'
        return mess 


if __name__ == '__main__':
    A = GrapheOriente()
    A.genereSommets()
    print(A.get_dico())
    A.ajouter_arc('B', 'A')
    A.ajouter_arc('C', 'A')
    A.ajouter_arc('B','C')
    A.ajouter_arc('D', 'A')
    print(A.successeurs('B'))


    