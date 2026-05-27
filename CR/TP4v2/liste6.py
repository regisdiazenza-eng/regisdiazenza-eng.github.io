liste =[2, 3, 5, 7]
demande = str(input("Souhaitez-vous ajouter(a) ou supprimer (s) un entier ? "))
n = int(input("A quel indice ? "))
if demande == "a" :
    liste.insert(n, int(input("Quel nombre entier ? ")))
    
elif demande == "s":
    del(liste[n])

print(liste)