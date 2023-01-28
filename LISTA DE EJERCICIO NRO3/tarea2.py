import os
texto="""”Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen.”"""
print(texto)
while(True):
    error = True
    while(error):
        print("""\nIngrese que transformacion desea aplicarle al texto:
    1) split
    2) join
    3) count
    4) find
    5) uppercase
    6) lowercase
    """)
        opcion = int(input("\n-------------------------->"))
        if(opcion==1 or opcion==2 or opcion==3 or opcion==4 or opcion==5 or opcion==6):
            error=False
        else:
            print("Seleccione una opcion correcta")
            error=True

    if opcion ==1:
        #convirtiendo a lista
        if type(texto)==list:
            print("El texto ya esta en forma de lista")
        else:
            texto=texto.split()
            print (texto)
    elif opcion ==2 :
        #sconvirtiendo a string
        if type(texto)==str:
            print("EL texto ya esta en forma de string")
        else:
            texto=" ".join(texto)
            print(texto)
    elif opcion ==3 :
        val=input("Ingrese la palabra que desea saber cuantas veces aparece:\n")
        print(texto.count(val))
    elif opcion == 4:
        val2=input("Ingrese la la palabra de la cual desea conocer su posicion:\n")
        print(texto.find(val2))
    elif opcion ==5 :
        if type(texto)==list:
            print("El texto debe estar en modo de string y no lista:")
        else:
            print("\nConvirtiendo a Mayuscula\n")
            texto=texto.upper()
        print(texto)
    elif opcion ==6 :
        if type(texto)==list:
            print("El texto debe estar en modo de string y no lista:")
        else:
            print("\nConvirtiendo a Minuscula\n")
            texto=texto.lower()
        print(texto)
    continuar = input("Desea continuar (S/N) ?")
    if(continuar =='n' or continuar == 'N'):
        break
os.system("cls")
print("gracias")