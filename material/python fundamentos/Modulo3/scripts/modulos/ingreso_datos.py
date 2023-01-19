
def ingreso_entero(msg: str="Ingrese un número entero: "):
    try:
        return int(input(msg))
    except:
        print('Dato incorrecto, vuelva a intentar ...')
        return ingreso_entero(msg)
    
def ingreso_decimal(msg: str="Ingrese un número decimal: "):
    try:
        return float(input(msg))
    except:
        print('Dato incorrecto, vuelva a intentar ...')
        return ingreso_decimal(msg)
    

# def ingreso(msg):
#     try:
#         return float(input(msg))
#     except:
#         print('Dato incorrecto, vuelva a intentar ...')
#         return ingreso(msg)

if __name__ == '__main__':
    entero = ingreso_entero()
    print(entero)