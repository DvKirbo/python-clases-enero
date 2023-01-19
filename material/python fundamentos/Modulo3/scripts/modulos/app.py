# 1. Importamos librerias

# import <nombre_archivo> |as <alias>
import ingreso_datos 
import ingreso_datos as ing

# from <nombre_carpeta> import <nombre_archivo> | as <alias>
from librerias import funciones_mate as mate
from librerias import triangulos

# 2. Declaración de constantes
MSG_BIENVENIDA = "Bienvenido al menú interactivo"
OPCIONES_MENU = """¿Qué quieres hacer? Escribe una opción
    1) Sumar dos numero
    2) Calcular el factorial de un número
    3) Indicar si numero es primo o no
    4) Mostrar un triangulo de altura h
    5) Salir
    """

# 3. Declaro funciones y/o clases

def opcion_1():
    # llamo <modulo|alias>.<funcion>
    num1 =  ing.ingreso_decimal("Ingrese el primero numero: ")
    num2 = ingreso_datos.ingreso_decimal("Ingrese el segundo número: ")
    
    s = num1 + num2
    print(f'La suma de los número {num1} + {num2} = {s}')
    pass

def opcion_2():
    
    n = ing.ingreso_entero()
    factorial = mate.factorial(n)
    
    print(f'{n}! = {factorial}')
    pass

def opcion_3():
    n = ing.ingreso_entero()
    primo = mate.valida_primo(n)
    
    if primo:
        print('El número es Primo')
        pass
    else:
        print('El número no es primo')
    pass

def opcion_4():
    
    h = ing.ingreso_entero('Ingrese la altura del triangulo: ')
    triangulos.mostrar_triangulo(h)
    
    pass


def main():
    
    # contiene la lógica principal
    print(MSG_BIENVENIDA)
    while True:
        opcion = input(OPCIONES_MENU) # me devuelve un string ''
        if opcion == '1':
            opcion_1()
        elif opcion == '2':
            opcion_2()
        elif opcion =='3':
            opcion_3()
        elif opcion=='4':
            opcion_4()
        elif opcion=='5':
            break
        else:
            print("Comando desconocido, vuelve a intentarlo")
    pass

# 4. Llamo a mi programa
if __name__ == '__main__':
    main()









