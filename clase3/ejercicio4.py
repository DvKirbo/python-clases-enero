#manejo de errorres
try:
    #m=8
    #n=int(input("ingrese numero para dividir a 8:\n"))
    #print(m/n)
    lista=[1,2,3]
    print(lista[5])
except Exception as e:
    #para saber que error ocurrio se usa Exception
    #para que no sea pesado su uso se le puede poner un modulo
    # Exception as e
    print(e)