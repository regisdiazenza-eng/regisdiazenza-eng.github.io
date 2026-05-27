ip = input("Adresse IP ? ")
adr_ip = ip.split(".")
if 0 <= int(adr_ip[0]) <= 127:
    print(f"L'adresse {ip} est de classe A.")
elif int(adr_ip[0]) <= 191:
    print(f"L'adresse {ip} est de classe B.")
elif int(adr_ip[0]) <= 223:
    print(f"L'adresse {ip} est de classe C.")
elif int(adr_ip[0]) <= 239:
    print(f"L'adresse {ip} est de classe D.")
else:
    print(f"L'adresse {ip} est de classe E.")