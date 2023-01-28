class Producto:
    def __init__ (self, nombre,marca,precio ):
        self.nombre=nombre
        self.marca=marca
        self.precio=precio
        self.enStock=True

    def __str__ (self):
        return "nombre: {}\n  marca: {}\n  precio: {}".format(self.nombre,self.marca,self.precio)
class Catalogo:
    def __init__ (self, listaProductos = []):
        self.listaProductos=listaProductos
        
    def adicionar (self, c):
        self.listaProductos.append(c)
        
    def mostrarCatalogo (self):
        print("Los productos del catalogo son:")
        for i ,j in enumerate(self.listaProductos):
            i+=1
            print(i,j)

p1=Producto ("waa","nintendont",999 )
catalogo=Catalogo()
catalogo.adicionar(p1)
catalogo.mostrarCatalogo()        