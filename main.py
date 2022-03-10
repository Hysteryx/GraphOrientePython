#utiliser webbrowser et un autre truc pour ouvrir avec le lien le code direct dedans
class GrapheOriente():


    def __init__(self, graph = {}) -> None:
        if graph == {}:
            self.graph = {}
        else:
            self.graph = graph

    def get_dico(self):
        '''Renvoie le dictionnaire de manière brut'''
        return self.graph

    def ajouter_sommet(self, sommet):
        '''Ajoute une sommet dans le graphe'''
        self.graph[sommet] = [] 
    
    def supprimer_sommet(self, sommet):
        '''supprime un sommet et ses liaisons (arc) dans le graphe'''
        try:
            all = self.predecesseurs(sommet)
            for i in range(len(all)):
                self.supprimer_arc(all[i],sommet)
            del self.graph[sommet]
        except:
            print("Sommet introuvable, merci de vérifier l'ortographe")

    def ajouter_arc(self, s1, s2):
        '''Ajoute une liaison dite arc entre deux sommets déjà existants'''
        try: 
            new = [self.graph[s1]][0]
            new.append(s2)
            self.graph[s1] = new 
        except:
            print('Un des deux sommets spécifiés ne semble pas exister !')

    def supprimer_arc(self,s1,s2):
        '''Supprime un arc'''
        try:
            new = [self.graph[s1]][0]
            del new[new.index(s2)]
        except:
           print('Un des deux sommets spécifiés ne semble pas exister !')

    def sommets(self):
        '''Renvoie la liste des tous les sommets'''
        sommets = []
        for i in self.graph.keys():
            sommets.append(i)
        return sommets

    def nb_sommets(self):
        '''Renvoie le nombre total de sommets'''
        return len(self.sommets())

    def nb_arcs(self):
        '''Renvoie le nombre total d'arcs'''
        cpt = 0 
        for i in self.graph.keys():
            cpt += len(self.graph[i])
        return cpt 

    def successeurs(self, sommet):
        '''Renvoie les successeurs d'un sommet spécifié'''
        try: return self.graph[sommet]
        except: print("Le sommet spécifié n'existe pas !")

    def predecesseurs(self, sommet):
        '''Renvoie les prédecesseurs d'un sommet spécifié'''
        try:
            l = []
            for v in self.graph.keys():
                if sommet in self.graph[v]:
                    l.append(v)
            return l 
        except:
            print("Le sommet spécifié n'existe pas !")

    def matrice(self):
        '''Renvoie la matrice du graph (binaire)'''
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
        '''Renvoie le code a inserer dans : http://www.webgraphviz.com/'''
        mess = 'digraph G {\n'
        if self.graph == {}:
            return "Le Graph Oriente ne contient aucun sommet !"
        for i in self.graph.keys():
            for k in range(len(self.graph[i])):
                mess += f"\"{i}\" -> \"{self.graph[i][k]}\"\n"
        mess += '}'
        return mess 


if __name__ == '__main__':
    pause, skip = False, False
    skip = False 
    asw = input("Dans l'objectif de rendre les test plus lisibles, voulez vous utiliser la fonction de séparation, vous devrez appuyez sur 'Entrer' entre chaque série de test, skip permet d'eviter les test de départ (oui/non/skip)\n>>>")
    if asw == 'oui' or asw == 'Oui' or asw == 'OUI':
        pause = True 
    if asw == 'skip':
        skip = True 
    if not skip:
        print('\n----- Creation du graphe, ajout de sommet et arcs-----\n')
        test = GrapheOriente()
        test.ajouter_sommet('A')
        test.ajouter_sommet('B')
        test.ajouter_sommet('C')
        print(test.get_dico()) 
        print('Ajout des arcs :\n')
        test.ajouter_arc('A','B')
        test.ajouter_arc('A','C')
        test.ajouter_arc('B','C')
        print(test)
        if pause : input('\nSuppression des arcs et sommets [ENTRER]\n')
        test.supprimer_sommet('A')
        print(test)
        print(test.get_dico()) #on constate la suppression des arcs liés au sommet 'A' 
        print("\n--on constate la suppression des arcs liés au sommet 'A'--\n")
        test.supprimer_arc('B','C')
        print(test)
        
        if pause: input('\nNous allons refaire un graph propre [ENTRER]\n')
        new = GrapheOriente()
        new.genereSommets(5) #cette méthode permet de générer 5 sommets dans l'ordre alphabétique 
        print(new.get_dico())
        print(new.sommets())
        print(new.nb_sommets())
        new.ajouter_arc("B","A")
        new.ajouter_arc('D','A')
        new.ajouter_arc('B','D')
        print('\n')
        print(new)
        print(new.nb_arcs())
        print('\n')
        print(new.successeurs('B'))
        print(new.predecesseurs('A'))
        if pause: input("\n-----Génération d'une matrice [ENTRER]-----")
        print(new.matrice())
    else:
        print('\n-----skipped-----\n')
    print("L'objectif est ici de casser la class\n")
    destroy = GrapheOriente()
    print('test de toutes les méthodes avec un graph vide :\n')
    print(destroy.get_dico())
    print(destroy.matrice())
    print(destroy.nb_arcs())
    print(destroy.nb_sommets())
    print('Test avec des arguments mauvais :')
    destroy.ajouter_arc('untruc','innexistant')
    destroy.supprimer_sommet('rienzoifn')
    destroy.supprimer_arc('le néant',"un autre néant")
    destroy.successeurs('nimp')
    destroy.predecesseurs('nimp')
    print('\n')
    destroy.genereSommets(10)
    destroy.supprimer_sommet('A')
    print(destroy.get_dico()) 
    print("\nAjout d'un graph directement :\n")
    jai_deja_un_dico = GrapheOriente({'A':['B','C','D'],
                                            'B':['A','D'],
                                            'C':['A','D','E'],
                                            'D':['A','B','C','E','F'],
                                            'E':['C','D','F'],
                                            'F':['D','E']})
    print(jai_deja_un_dico)
    print(jai_deja_un_dico.get_dico())
    print(jai_deja_un_dico.sommets())
    print(jai_deja_un_dico.nb_arcs())
    print(jai_deja_un_dico.nb_sommets())
    jai_deja_un_dico.supprimer_sommet('A')
    print(jai_deja_un_dico)
    print(jai_deja_un_dico.get_dico())
