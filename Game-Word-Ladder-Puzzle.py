import random as rd

def lettre_commun(mot1,mot2):
    n=0
    for i in range(len(mot1)):
        if mot1[i] == mot2[i]:
            n+=1
    if len(mot1)-1 == n:
        return True
    else:
        return False

def adjacence(dico,nb):
    graph = {}
    for parent in dico[nb]:
        graph[parent] = []
        for enfant in range(len(dico[nb])):
            test = lettre_commun(parent, dico[nb][enfant])
            if test == True:
                graph[parent].append(dico[nb][enfant])
    
    return graph

def BFS(entre,graph):
    ouvert = [entre] #sommets à visiter
    ferme = [] #sommets déjà visité
    parents = {}
    parents[entre] = None
    while ouvert != []:
        tmp = ouvert.pop(0)
        if tmp not in ferme:
            ferme.append(tmp)
        for i in graph[tmp]:
            if i not in ouvert and i not in ferme:
                parents[i] = tmp
                ouvert.append(i)
    return parents

def chemin(graph, debut, fin):
    solution = []
    parent = BFS(debut,graph)
    sommet = fin
    while parent[sommet] != None:
        solution.append(sommet)
        sommet = parent[sommet]
        
    solution.append(debut)
    solution.reverse()
    return solution

def demander(mot, dico, longueur, debut, fin):
    solution = [debut]
    good = False
    while True:
        while good != True:
            print(f"Vous devez aller de {debut} à {fin}")
            print(f"Vous êtes au mot {mot}")
            ask = input("Quel est votre prochain choix ?")
            if ask == "!aide":
                print("")
                print(f"Les mots reliés à {mot} sont {dico[mot]}")
            elif ask == "!solution":
                print("Vous avez perdu")
                print(f"Le bot avait trouvé {reponse}")
                return None
            else:
                try:
                    dico[ask]
                    if lettre_commun(ask, mot) == True:
                        if len(ask) > longueur:
                            print("/!\Le mot est trop grand/!\'")
                        elif len(ask) < longueur:
                            print("/!\Le mot est trop petit/!\'")
                        elif ask == fin:
                            solution.append(ask)
                            print(" ")
                            print("Bravo ! Vous avez gagné !")
                            print(f"Le bot avait trouvé {reponse}")
                            print(f"Vous avez trouvé {solution}")
                            return None
                        else:
                            good = True
                except:
                    print("  ")
                    print("/!\Ce mot n'existe pas/!\'")
                
                print("  ")
        good = False
        mot = ask
        solution.append(ask)

file = open("words.txt", "r").read().split("\n")
dico = {}
for mot in file:
    if len(mot) in dico:
        dico[len(mot)].append(mot)
    else:
        dico[len(mot)] = [mot]

taille = int(input("Quelle est la taille du mot ?"))
while True:
    debut = rd.choice(dico[taille])
    fin = rd.choice(dico[taille])
    graphique = adjacence(dico,taille)
    try:
        reponse = chemin(graphique, debut, fin)
        break
    except:
        pass
    
mot = debut
demander(mot, graphique, taille, debut, fin)