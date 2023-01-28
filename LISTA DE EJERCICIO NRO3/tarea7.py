""".Programa que tenga una clase Producto el cual solo tiene el atributo de nombre ,codigo
el cual tiene la siguiente estructura PAIS-LOTE-AÑO ejemplo : PERU-0001-2023 crear un
método que permita imprimir el objeto de forma literal (__str__) y que me permita identificar
el país de origen , el numero de lote"""

class Producto:
    def __init__ (self, pais, lote ,year):
        self.pais=pais                
        self.lote=lote
        self.year=year
        
    def __str__ (self):
        return(f"{self.pais}-{self.lote}-{self.year}\nPais de origen: {self.pais}\nNumero de lote: {self.lote}") #__str__ siempre debe devolver un str , si se usa un print sale error 

p1=Producto("Peru", "0125","2022")
print(p1)