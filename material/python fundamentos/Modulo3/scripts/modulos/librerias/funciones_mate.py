

def factorial(n:int):
    if n<0:
        # error personalizado
        raise ValueError("Negativos no permitidos")
    
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
        pass
    return fact

def factorial_recursivo(n:int):
    if n==1:
        return 1
    else:
        return n * factorial_recursivo(n-1)


def valida_primo(n):
    """A partir de un numero "n" dado, evalua si es primo o no"""
    # Busco divisores en el rango de [2; numero-1]
    
    assert n>=1 # Arroja error si no se cumple la condicion
    
    es_primo =True
    for num in range(2, n):
        if n % num == 0:
            es_primo=False
            break # salgo del bucle
    return es_primo # retorno True, False

if __name__ == '__main__':
    
    # pruebas
    # print(factorial(5))
    # print(factorial(0))
    # print(factorial(-2)) # debería dar error
    
    # pruebas func primo
    print(valida_primo(8)) #
    print(valida_primo(7))
    print(valida_primo(-5))
    
    