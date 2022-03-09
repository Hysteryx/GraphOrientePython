
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
        pass 

    def predecesseurs(self, sommet):
        pass 

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

    def __str__(self) -> str:
        mess = ''
        if self.graph == {}:
            return "Le Graph Oriente ne contient aucun sommet !"
        for i in self.graph.keys():
            mess += f"{i}-->{self.graph[i]}\n"
        return mess 


if __name__ == '__main__':
    A = GrapheOriente()
    """
    A.ajouter_sommet('test')
    print(A)
    A.get_dico() #mettre un print si ça s'affiche pas sur vscode 
    A.supprimer_sommet('test')
    print(A)
    """
    A.ajouter_sommet('A')
    A.ajouter_sommet('B')
    A.ajouter_arc('A','B')
    print(A)
    A.ajouter_sommet('C')
    A.ajouter_arc('A','C')
    print(A)
    A.supprimer_arc('A','C')
    print(A)
    print(A.sommets())
    print(A.nb_sommets())
    print(A.nb_arcs())
    print(A.matrice())