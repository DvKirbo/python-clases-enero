numero = int(input("ingrese un numero: "))
isPrimo=False
for i in range (2, numero +1):
    if numero%i==0:
        isPrimo = True
        break
if isPrimo:
    print("El numero es primo")
else:
    print("El numero no es primo")