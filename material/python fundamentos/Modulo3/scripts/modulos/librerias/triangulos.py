

def mostrar_triangulo(altura:int, simbolo="#"):
    
    # valido altura positiva
    assert altura>=1
    
    for i in range(altura):
        print(simbolo* (i+1))