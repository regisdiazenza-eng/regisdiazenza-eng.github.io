demande = str(input("Quel conversion voulez-vous faire ? "))
if demande == "cel_to_fah":
   cel = float(input("celsius : "))
   print(f"fahrenheit = {cel*1.8+32:.2f}")
elif demande == "fah_to_cel":
   fah = float(input("fahrenheit : "))
   print(f"celsius = {(fah-32)/1.8:.3f}")