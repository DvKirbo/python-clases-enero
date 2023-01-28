def saludarFuncion ():
    print("hola te saludo desde la funcion saludar, del modulo saludos")
    
def sumaNumeros (a,b):
    print("los numeros",a,b)
    return a+b

def names():
    print("desde archivo de libreria", __file__,"=>",__name__)
    
    
if __name__=='__main__':
    print("estas en el archivo principal")
else:
    ("archivo de libreria")