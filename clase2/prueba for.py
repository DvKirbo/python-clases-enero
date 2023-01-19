lista = ["juan", "jose", "sebastian", "alberto"]
for nombre in lista:
    print(nombre)
    
for i in enumerate(lista):
    print(i)
    
#enumerate(enumera los elementos de un array)
for i , nombre in enumerate(lista):
    print(i)
    print(nombre)
    print(i, nombre)