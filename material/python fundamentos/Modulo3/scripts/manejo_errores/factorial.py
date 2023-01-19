

def ingreso_entero(msg: str = "Ingrese un número entero: "):
    """Solicitar un número entero al usuario

    Args:
        msg (str): Mensaje a usuario. Defaults to "Ingrese un número entero: ".

    Returns:
        int: 
    """
    try:
        return int(input(msg))
    except:
        return ingreso_entero(msg)


def factorial(n:int):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
        pass
    return fact


num = ingreso_entero()
if num >=0:
    print(f'El factorial de {num}! es ', factorial(num))
else:
    print('No se permiten número negativos')