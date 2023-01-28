import sys
argumentos =sys.argv
print(argumentos)

def leerargumentos(*args):
    for arg in args:
        print (arg)
        
leerargumentos(*argumentos)#el asterisco es por q argumentos es una lista
#nota //sys.argv es una lista
print(type(argumentos))