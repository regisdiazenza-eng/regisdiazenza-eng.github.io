from random import(randint)

def adresses_ip(classe:str="A") -> str:
    adr = [i for i in range(4)]
    if classe=="A":
        adr[0] = randint(0,127)
    elif classe=="B":
        adr[0] = randint(128,191)
    elif classe=="C":
        adr[0] = randint(192,223)
    elif classe=="D":
        adr[0] = randint(224,239)
    else:
        adr[0] = randint(240,255)
    for i in range(1,4):
        adr[i] = randint(0,255)

    return f"{adr[0]}.{adr[1]}.{adr[2]}.{adr[3]}"



def classe(adresse:str) -> str:
    premier_octect = int(adr.split(".")[0])
    if 0 <= premier_octect <= 127:
        classe:str="A"
    elif 128 <= premier_octect <= 191:
        classe:str="B"
    elif  192 <= premier_octect <=223:
        classe:str="C"
    elif  224 <= premier_octect<= 239:
        classe:str="D"
    else:
        classe:str="E"
    return classe

if __name__ == "__main__":
    adr = adresses_ip("E")
    print(f"{adr} est de classe {classe(adr)}")
