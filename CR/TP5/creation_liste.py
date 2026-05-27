from random import randint

def liste_utilisateur(n=5):
    liste =[i for i in range(n)]
    for p in range(n):
        liste[p] = int(input(f"liste[{p}] = "))
    return liste


def liste_aleatoire(n=5, bornemin=0, bornemax=100):
    liste =[i for i in range(n)]
    for c in range(n):
        liste[c] = randint(bornemin,bornemax)
    return liste

l1 = liste_utilisateur(4)
print(l1)
l2 = liste_aleatoire(4)
print(l2)