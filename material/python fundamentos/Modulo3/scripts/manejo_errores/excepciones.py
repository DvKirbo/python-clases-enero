


try:
    n = int(input('Ingrese un numero: '))
    print(7/n)
except ZeroDivisionError:
    print('No se permite el ingreso de 0')
except Exception as e:
    print(e)
    #print('Sucedio otra cosa')