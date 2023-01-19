# Realizar un codigo que permita conocer a los numeros primos entre el 1 y el 100

# listado_primos = []

# for numero in range(1, 101):
    
#     # Busco divisores en el rango de [2; numero-1]
#     es_primo =True
#     for num in range(2, numero):
#         if numero % num == 0:
#             es_primo=False
#             break # salgo del bucle
    
#     # Si resultado fue True
#     if es_primo:
#         listado_primos.append(numero)
#         pass

# print(f'Listado de Primos: {listado_primos}')
    
        
# def -> definir función
# función es aquella que contiene cierta lógica
def valida_primo(n):
    """A partir de un numero "n" dado, evalua si es primo o no"""
    # Busco divisores en el rango de [2; numero-1]
    es_primo =True
    for num in range(2, n):
        if n % num == 0:
            es_primo=False
            break # salgo del bucle
    return es_primo # retorno True, False

# 1. Evaluare el rango de numeros entre 1 al 100
listado_primos = []
for numero in range(1, 101):
    # 2. Si es Primo, añado numero al listado
    if valida_primo(numero):
        listado_primos.append(numero)
        pass
# 3. Imprimo listado
print(f'Listado de Primos: {listado_primos}')
