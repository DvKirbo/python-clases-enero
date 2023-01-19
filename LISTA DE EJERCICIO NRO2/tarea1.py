import os
#realizar un menu iterativo: seleccionar con numeros
#""
# 1)realizar un programa que realice un cuadrado en consola con * usando bucles
# 2)realizar una iteracion de una lista de numeros e identificar si es multiplo de 2 e imprimir el numero
# 3) iterar una lista de elementos que tengan nombre y edad y sol imprimir los mayores de edad
# cada elemento de la lista puede ser otra lista [nombre; edad]""
msg="""
1)realizar un programa que realice un cuadrado en consola con * usando bucles
2)realizar una iteracion de una lista de numeros e identificar si es multiplo de 2 e imprimir el numero
3)Iterar una lista de elementos que tengan nombre y edad; y solo imprimir los mayores de edad
4)Salir
"""

while(True):
    print(msg)
    opcionMenu= int(input("Seleccione una opcion:\n"))
    
    if(opcionMenu != 1 and opcionMenu != 2 and opcionMenu != 3 and opcionMenu!=4):
        print("Seleccione una opcion correcta")

    elif opcionMenu==1:
        tcuadrado=int(input("Ingrese el tamaño del cuadrado: \n"))
        os.system("cls")
        for i in range (tcuadrado):
            for j in range (tcuadrado):
                print("*    ",end="")
            print("\n")
        
    elif opcionMenu==2:
        lista=[]
        n=int(input("Ingrese cuantos numeros va a examinar: "))
        os.system("cls")
        for i in range (n):
            numero=int (input("Ingrese los numeros que va a examinar:\n"))
            lista.append(numero)
        os.system("cls")
        print(lista)
        print("Los multiplos de 2 son: \n")
        for x in range (n):
            if lista [x]%2==0:
                print(lista[x])
                
    elif opcionMenu==3:
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
        print("son mayores de edad:")
        for x,y in (lista2):
            if y>=18:
                print(x,y)
    elif opcionMenu==4:
        print("Gracias")
        break
                