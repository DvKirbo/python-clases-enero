import sys
print(sys.argv)

n= int(input("ingrese un numero:\n"))
aux=0
for i in range (n+1):
    aux+=i
print(aux)
