from lib.libfile import saludarFuncion, sumaNumeros

#para importar todas la funciones de un archivo importado se usa el*
from lib.libfile import *
from POOPython import *
import os

#si se importa sin el from seria
#import lib.libfile
#lib.libfile.saludarFuncion()


#tmbn se le puede importar como un modulo para evitar fatiga
#import lib.libfile as lib
#lib.saludarfuncion()


#es como las namespaces en c++
#waos

saludarFuncion()
sumaNumeros(4,5)

c3= Celular ("apple", "retina45.7565", "chi687568456", "15.46.89")
print(c3)

#nota el pycache guarda , archivos o cache para que se importe mas rapido las librerias
#cache = memoria de rapido accseso

print(__file__,"=>",__name__)
names()

if __name__=='__main__':
    print("estas en el archivo principal")
else:
    ("archivo de libreria")
    print(os.getcwd())