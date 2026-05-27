liste=[]
liste.append(str(input("Nom de votre machine : ")))
liste.append(int(input("RAM (Go) : ")))
liste.append(float(input("CPU (GHz) : ")))
print(f"La liste contient : {liste}")

liste=[]
liste += [str(input("Nom de la machine : "))] + [int(input("RAM (Go) : "))] + [float(input("CPU (GHz) : "))]
print(liste)

liste =[]
liste.insert(0, str(input("Nom de votre machine : ")))
liste.insert(1, int(input("RAM (Go): ")))
liste.insert(2, float(input("CPU (GHz) : ")))
print(liste)