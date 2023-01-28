class Catalogo:
    def __init__(self, listacelulares = []):
        self.listacelulares = listacelulares
        
    def agregar (self,c):
        self.listacelulares.append(c)
    def mostrarCatalogo (self):
        print("Los celulares en catalogo son:")
        for i,j in enumerate(self.listacelulares):
            i+=1
            print(i,j)
class Celular:
    #necesitamos un constructor: __init__
    #constructor//funcion que inicializa nuestra clase cuando se convierta a un objeto//self -> hace referencia a la clase
    #le damos los atributos que nos interesen
    
    #             self es un argumento que hace referencia a asi mismo (la clase)
    def __init__ (self, marca,pantalla, imei,camara):#nota como son parametros se les puede poner cualquier nombre, pero por convencion se le pone el mismo o cambiado la ultima letra para evitar errores en el codigo
        self.marca=marca
        self.pantalla=pantalla
        self.imei=imei
        self.camara=camara
        self.activado=False
        self.apagado = True
        self.pantallaBloqued=False
        
    def __str__ (self):
        return f"El celular tiene los  sgtes atributos {self.marca} , {self.pantalla} , {self.imei} , {self.camara}"
    def sizeDisplay (self):
        descripcion=self.pantalla.split(sep='-')
        return float(descripcion[1])
    def camaraFrontal (self):
        camarafrontal = self.camara.split(sep=",")
    def activar (self, name):
        print(name)
        self.activado=True
    def estado (self):
        if self.activado:
            return "celular activado"
        else:
            return "celular desactivado"
    def estadoPantalla (self):
        if self.apagado:
            print("El celular se encuentra apagado")
        else:
            print("El celular se encuentra prendido") 
    
    def bloquearPantalla (self):
        self.pantallaBloqued=True
    
    def prender (self):
        self.apagado=False
    def apagar (self):
        self.apagado=True
    
try:
    c1=Celular("nokia", "retina-6.4", "chi987564564", "8,4,3")
    c2= Celular("lg", "hd6-2", "jyhe684569874", "7,2,3")
    catalogo = Catalogo()
    catalogo.agregar(c1)
    catalogo.agregar(c2)
    catalogo.mostrarCatalogo()
    
    print(c1.__str__())
    c1.activar("sebas")
    a=c1.estado()
    print(a)
    c1.estadoPantalla()
    catalogo= [c1,c2]
    for i in catalogo:
        print(i)
    
except Exception as e:
    print("error al crear los objetos de los celulares")
    print(e)






#para encapsular se usa __nombre// para metodos y atributos
#acceso restringido 

#getters y setters

#get //obtener
#set // establecer

#nota// python solo simula los metodos public y private
#en si todos los metodos y funciones de python son publicos
