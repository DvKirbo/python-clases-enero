#pass//vacio
#opcional
def mifuncion ():
    print("hola")
    
#solo lo hemos definido falta llamarlo
mifuncion()
#aca ya lo estamos llamando

def funcionconretorno():
    return("hola")
msg=funcionconretorno()
print(msg)

def funcionparametro1(a):
    return a

def funcionparametro2 (b):
    return b
def funcionparametro3 (c="default"):
    print(c)

funcionparametro1(2)
x=funcionparametro2(3)
print(x)
funcionparametro3()