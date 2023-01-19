def maxval (n1, n2):
    if n1>n2:
        return ("El mayor numero es:"+str(n1))
    elif n2>n1:
        return ("El mayor numero es:"+str(n2))
    else:
        return "Ambos numeros son iguales"
    
n1=int(input("Ingrese un numero: \n"))
n2=int(input("Ingrese otro numero: \n"))
mayor=maxval(n1,n2)
print(mayor)