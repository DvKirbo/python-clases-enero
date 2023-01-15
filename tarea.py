#Sebastian Antonio Cueto Salazar
print("Ejercicio 1")
nombre=input("Ingrese su nombre\n")
edad=(int(input("Ingrese su edad\n")))
print("Sus datos personales son:")
print(f"Nombre: {nombre}\nEdad: {edad}\n\n")

print("Ejercicio 2")
pi=3.1416
print("Hallando area del circulo")
r=float(input("Ingrese la longitud del radio del circulo:\n"))
a_circ=pi*(r**2)
print(f"el area del circulo es: {a_circ}")
print("Hallando el area del traingulo:")
b=float(input("Ingrese la longitud de la base:\n"))
h=float(input("Ingrese la longitud de la altura:\n"))
a_triang=(b*h)/2
print(f"El area del traingulo es: {a_triang}")
l=float(input("Ingrese el la longitud de uno de los lados del cuadrado:\n"))
print("el area del cuadrado es: ", l**2)
print("\n\n")

print("Ejercicio 3")
val1=int(input("Ingrese un numero: \n"))
val2=int(input("Ingrese otro numero: \n"))
val3=int(input("Ingrese un tercer numero: \n"))
print("La suma de los valores es: ",val1+val2+val3)
print("La resta de los valores es: {} , {} , {} , {} , {} ,{} ".format(val1-val2, val1-val3,val2-val1, val2-val3, val3-val1, val3-val2))
print("La multiplicacion de los 3 valores es: ",val1*val2*val3)
print(f"La division de los 3 valores es: {val1/val2} , {val1/val3} , {val2/val1} , {val2/val3} , {val3/val1} , {val3/val3}" )
print(f"La division exacta de los 3 valores es: {val1%val2} , {val1%val3} , {val2%val1} , {val2%val3} , {val3%val1} , {val3%val3}\n\n")

print("Ejercicio 4")
valor =input("Ingrese cualquier valor:\n")
print("el tipo de dato ingresado es: ", type(valor))

print("Ejercicio 5")
import sys
ubicacion = sys.argv
print(f"La ubicacion del archivo actual es: {ubicacion}\n\n")

print("Ejercicio 6")
n= int(input("ingrese un numero:\n"))
suma=n(*(n+1))/2
    
print("Ejercicio 7")
a=int(input("Ingrese un numero:\n"))
b=int(input("Ingrese otro numero:\n"))
if a==b:
    print("Los numeros son iguales:\n")
if a!=b:
    print("Los numeros son diferentes\n")
    if a>b:
        print("El primero es mayor que el segundo\n")
    if a<b:
        print("El segundo es mayor que el primero\n")
        
print("Ejercicio 8")
password="contraseña"
password_min =password.lower()#convertimos la contraseña en minusculas
contra_usuario = input("Ingrese la contraseña:\n")
contra_usuario_min = contra_usuario.lower()#convertimos la contraseña con la que vamos a comparar en minusculas tambien}#De modo que al estar ambas en minusculas se le puede comparar sin importar como estaban escritas inicialmente
if(password_min==contra_usuario_min):
    print("Las contraseñas coinciden")
else:
    print("Las contraseñas no coinciden")
