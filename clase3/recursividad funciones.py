#funciones que se llaman a si misma

#ejemplo con el factorial de un numero:

def factorial (n):
    if(n==1):
        return 1
    else:
        return n*factorial(n-1)

a=factorial(5)
print(a)

#otro ejemplo

def juego (intentos:int=1):
    respuesta = input("¿DE que color es la naranja?")
    if respuesta.lower()!="naranja":
        if intentos < 3:
            print("Fallaste intentalo de nuevo")
            intentos+=1
            juego(intentos)#recursividad
        else:
            print("perdiste")
    else:
        print("ganaste")