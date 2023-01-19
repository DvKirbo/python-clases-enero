a=["Hola",1]
b=["asd",2]
c=[a,b]
print(c[0][1])

for x,d in (c):
    print(x,d)

n= int(input("Ingrese cuantas personas se van a analizar:\n"))
lista2 = []
#creador de listas
for i in range (n):
    lista = list()
    nombre = str(input("ingrese el nombre: \n"))
    edad = int(input("ingrese su edad: \n"))
    lista.append(nombre)
    lista.append(edad)
    print(lista)
    #guardamos las listas creadas en otra lista
    lista2.append(lista)
print(lista2)
print("son mayores de edad: \n")
for x,y in (lista2):
    if y>=18:
        print(x,y)

#intentar esto en c++