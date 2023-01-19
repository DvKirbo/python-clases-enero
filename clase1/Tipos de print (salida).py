suma=7+3
val1="todos"
val2=("lima")
#opcion 1
print("el valor de la suma es "+ str(suma))#solo se pueden sumar vars del mismo tipo
#opcion 2//mejor opcion
print(f"el valor de la suma es: {suma}")#formatea el numero a texto

#opcion 3
print("el valor de la suma es {} y las variables son {}  y {}".format(suma, val1, val2))