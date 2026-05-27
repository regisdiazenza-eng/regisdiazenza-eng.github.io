mot = str.lower(input("Mot: "))
if mot[::-1] == mot :
    print(f"{mot} est un palindrome.")
else :
    print(f"{mot} n'est pas un palindrome.")