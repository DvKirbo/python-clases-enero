#FOR//  

#trabaja sobre arrays// for var in array:recorre los elementos del array

for x in range (1,11,2):#(inicio, final, cantidad )
    print (x)
    
numeroIteraciones= int(input("Ingrese cuantos numeros desee iterar: "))
numeros = list()#se crea lista vacia

print(numeros)
for i in range (1,numeroIteraciones+1):
    if i%2==0 and i%3==0 and i%5!=0:
        numeros.append(i)
print(numeros)

#for i, nombre in enumerate (lista):
#   print(i, nombre)