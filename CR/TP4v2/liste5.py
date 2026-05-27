n = int(input("Nombre d'entiers ? "))
liste = [i for i in range(n)]
for i in range(n):
    liste[i] = int(input(f"liste{[i]} = "))
print(f"Liste créée : {liste}")