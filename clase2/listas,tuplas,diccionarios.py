#colecciones de datos python//arrays

#definir lista vacia // lista= []
# //otra forma // list()


#cantidad de elementos len()

#ultimo elemento de la lista lit[-1]

#.append(var)//agrega una variable al final de la lista

#.count(var)//cuenta cuantas veces se repite una variable en la lista

#.reverse()//revierte el orden de una lista

#.remove(var)//elimina un elemento de la lista
#.pop()

#.index(var)//brinda la posicion de una variable dentro de la lista


lisa = [1,2,3,4,5,7]
lisa.find(5)
#mutabilidad = alterar listas

#navegacion entre indices: {n:}//donde n seria el inicio
#se van a mostrar la lista a partir del elemento n
#[inicio:fin:saltos]
numeros = [1,2,3,4,5]
print(type(numeros))
print(numeros)
print(numeros[2:4])

#tuplas => son lo mismo peroson inmutables
#a menos que las cambies en el inicio cuando se declaran

#diccionarios {}
#estructuras mapeadas//strings asociados valores

#Diccionario vacio: dict()// vacio = {}

#definiendo diccionarios

diccionario = {
    "key1":12,
    "key2":"hola",
}
print(diccionario)

#buscando valor por clave dentro de diccionarios//clave = keys = strings
print(diccionario["key1"])
print(diccionario["key2"])

#mutabilidad
diccionario["key2"]=25
print(diccionario["key2"])
print(diccionario)

#si se le asigna un valor a un key que no existe , este se crea automaticamente
diccionario["key3"]=87
print(diccionario)

#las listas pueden tener diccionarios
lista = [1,2,3,4,5,diccionario]
print(lista)

#listas dentro de diccionarios
dict2 ={
    "colegio":"liceo naval",
    "Notas": [1,2,3,4,5,6,7,8,9,10]
}
print(dict2)
print(dict2["Notas"][0])
lista.append(dict2)
print(lista)

#METODOS DE DICCIONARIOS

#.keys()//imprime las llaves
print(dict2.keys())

#.values()//imprime las llaves
print(dict2.values())

#items//keys y values
print(dict2.items())

#CONJUNTOS
#.set()
#para declarar un conjunto se usa set()
conjunto= set()
print(conjunto)
conjunto ={1,2,3,4,4,5,6,89,7}
print(conjunto)
