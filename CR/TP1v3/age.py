nom = str(input("Nom : "))
age = int(input("age : "))
if 64 < age :
    print(f"{nom} a droit de prendre sa retraite")
elif 18 < age :
    print(f"{nom} peut voter")
elif 16 < age :
    print(f"{nom} peut apprendre à conduire")
elif 14 < age :
    print(f"{nom} peut avoir une trottinette électrique")
else :
    print(f"{nom} peut jouer au marché de Padi Pado")