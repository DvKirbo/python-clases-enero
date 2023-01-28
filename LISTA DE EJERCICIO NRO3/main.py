#EJERCICIO 1,5 Y 8
from lib.lib import *
import os

if __name__=='__main__':
    print("Estas en el archivo principal")
else:
    print("Estas en una dependencia")
    
try:
    pass
    n=int(input("Ingrese hasta que numero desea sumar los numeros:\n"))
    a=suma_N_numeros(n)
    print("La suma es:", a)
    opcion=True
    while(opcion):
        print("Ingrese 2 numeros para dividir")
        n1=int(input("Ingrese un numero:\n"))
        n2=int(input("Ingrese otro numero:\n"))
        if n2==0:
            print("ingrese un numero diferente a 0")
        else:
            opcion =False
    
    div=division(n1,n2)
    print("la division de los numeros es:", div)
    
    #EJERCICIO 6
    print("El nombre del archivo es",__file__, "====>",__name__)
except Exception as e:
    print("hubo un error")
    print(e)
else:
    print(os.getcwd())
finally:
    print("proceso terminado")