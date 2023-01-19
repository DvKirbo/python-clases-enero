import os
biblioteca = {
    "categorias":["Amoroso","Histórico","Aventuras","Policial","Fantástico","terror","comics","poesia","manga"],
    "nombres_autores":{
        "autores":["Miguel de Cervantes","Agatha Chistie","Charles Dickens","Federico García Lorca","Gabriel García Márquez","Ernest Hemingway","Victor Hugo","James Joyce","Yusuke Murata","Hideo Kojima","ONE","Araki"],
        "nombres":["mob psycho", "Jojos Bizarre adventure","Mob psycho","Cien años de soledad","El señor de los anillos","1984","Un mundo feliz","Orgullo y prejuicio","Crimen y castigo"]
    },
    "estado de los libros":"No prestado",
    "lista de usuarios":["Juanito alcachofa", "Jenifer Coronado","Dolores del sano","Ascension Teruel","Celestino Madrid","Hamza Tomas","Jorge mitales","giorno giovanna","peter parker","senku ishigami","jhonathan joestar"]
}
msg="""Bienvenido a la biblioteca:
1)Obtener lista de la categoria de libros
2)Obtener nombres de libros y autores
3)Cambiar el estado de un libro a prestado
4)Lista de usuarios de la biblioteca"""
print(msg)
opcion = int(input("Seleccione una opcion:\n"))
if opcion !=1 and opcion!=2 and opcion !=3 and opcion !=4:
    print ("error")
elif opcion==1:
    os.system("cls")
    print("Las categorias de los libros son: \n")
    for i in biblioteca["categorias"]:
        print(i)
elif opcion==2:
    os.system("cls")
    print("Los autores son: ")
    for i in biblioteca["nombres_autores"]["autores"]:
        print(i)
    print("\n")
        
    print("Y los nombres de los libros son: \n")
    for i in biblioteca["nombres_autores"]["nombres"]:
        print(i)
        
elif opcion==3:
    os.system("cls")
    print("El estado del libro es: ", biblioteca["estado de los libros"])
    llevar=(input("Desea tomar el libro prestado? (S/N)\n"))
    if llevar=="s" or llevar == "S":
        biblioteca["estado de los libros"]="Prestado"
        print("El estado del libro es: ", biblioteca["estado de los libros"])
    else:
        print("El estado del libro es: ", biblioteca["estado de los libros"])
elif opcion==4:
    os.system("cls")
    print("los usuarios son:\n")
    for i in biblioteca["lista de usuarios"]:
        print(i)