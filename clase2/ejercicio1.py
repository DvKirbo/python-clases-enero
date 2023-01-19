#introducir 2 numeros
n1 = int (input("Introduzca un numero:\n"))
n2 = int(input("Introduzca otro numero: \n"))
msg="""Elija una de las siguientes opciones:
1)Mostrar la suma de los 2 numeros.
2)Mostrar la resta de los 2 numeros (El 1ro menos el 2do).
3)Mostrar la multiplicacion de los 3 numeros.
----------------------------------------------------------
"""
print(msg)

opcion = int(input("seleccione una opcion").upper())
if opcion !=1 or opcion!=2 or opcion !=3:
    print("seleccione una opcion correcta")
elif opcion==1:
    print("La suma es: ", n1+n2)
elif opcion ==2:
    print("la restas es: ",n1-n2 )
elif opcion==3:
    print("la mutiplicacion es: ",n1*n2 )
