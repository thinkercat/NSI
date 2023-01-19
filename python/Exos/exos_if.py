#EX plus grand
valeur1 = int(input("Premier nombre :"))
valeur2 = int(input("Deuxieme nombre : "))

if valeur1 < valeur2:
    print(valeur2, "est le plus grand")
elif valeur1 == valeur2:
    print("Les deux nombres sont égaux")
else:
    print(valeur1,"est le plus grand")

#EX divisible
print("\n-*- Verificatoin de division -*-")
nombre1 = int(input("Premier divisible : "))
nombre2 = int(input("Deuxieme divisible : "))
for nombre in range (1,1001):
    if nombre % nombre1 == 0 and nombre % nombre2 == 0:
        print(f"{nombre} est divisible par {nombre1} et {nombre2}")