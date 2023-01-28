#FUNCIONES PARAMETROS 2
#cuando no se sabe la cantidad de parametros q se le va a subir a la funcion

#def funcion(*args)
#args => "hola",5,789.5, etc
#args es un diccionario local con numero indefinido de items
#normalmente son del mismo tipo
#se le puede poner cualquier nombre en lugar de args// lo importante es que lleven el '*'

def funcion (*args):
    for arg in args:
        print(arg)
        
funcion("hola", [1,2,3,4,5,6,7],"asd",5,{"dia":"sabado"})

#Kwargs// 
#igual q en args se le puede remmplazar por cualquier nombre mientras tenga los '**'

#diccionario local con un número indeterminado de valores. 
#Es necesaria cuando deseamos realizar una función que tenga los parámetros que deseamos, aunque no sean ni del mismo tipo o no tengan el mismo significado


#CUANDO EL PARAMETRO ES UNA LISTA   
# valores a ser sumados se encuentran en una lista
def sumar(a,b):
    return a+b

# lista con valores a ser sumados
numeros_sumar=[23,11]

print(sumar(*numeros_sumar))
#cuando se quiera usar una lista por parametro sin desempaquetar los datos se usa:
#   funcion(*lista)//sin el '*' no funciona

sumar(numeros_sumar[0],numeros_sumar[1])


#PARAMETROS GLOBALES Y LOCALES
#para cambiar una variable a nivel global se usa global

#global var
x=7

def cambio_nivel_global():
    global x    #con esto se reasigna la variable a nivel global
    x=4
    print(x)
    
cambio_nivel_global()
print(x)