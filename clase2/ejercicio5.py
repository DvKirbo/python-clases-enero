#minissistema de notas
#diccionario
sistema={
    "NombreDeInstitucion":"colegioN",
    "aulas":["python","javascript", "java,php"],
    "profesores":["Profesor1","profesor2"],
    "alumnos":{#diccionarios indentados
        "7553":{"nombre":"juan",
                "apellido":"rodriguez",
                "cursos":["python"],
                "notas":{}
                },
        
        "8225":{"nombre":"juan",
                "apellido":"rodriguez",
                "cursos":["python", "javascript"],
                "notas":{}
                },
        
        "7543":{"nombre":"juan",
                "apellido":"rodriguez",
                "cursos":["php"],
                "notas":{}
                }
    },
    "cursoprofesor":{
        "python":[],
        "php":[],
        "c++":[],
        "javascript":[]
    }
}

#asignar profesor cursos
profesoresactuales= sistema["profesores"]
profesorporasignar = input("que profesor es?")
if profesorporasignar in profesoresactuales:
    print("existe el profesor")
    print(sistema["cursos"])
    cursoporasignar = input("QUe curso va a asignar el profesor?")
    if cursoporasignar in sistema["cursos"]:
        cursotemp = sistema["cursoprofesor"][cursoporasignar]
        cursotemp.append(profesorporasignar)
        sistema["cursoprofesor"][cursoporasignar]=cursotemp
    else:
        print("no existe el curso")
else:
    print("No existe el profesor debe agregarlo")
    print(profesorporasignar,sistema["profesores"])
    profesortemp=sistema["profesores"]
    profesortemp.append(profesorporasignar)
    sistema["profesores"]=profesortemp
    print(sistema)
    
 #asignar nota alumno
codalumno = input("ingrese el codigo de alumno")
listaalumnos = list(sistema["alumnos"].keys())
if codalumno in listaalumnos:
    print("alumno existe")
    cursodealumno = sistema["alumnos"][codalumno]
    notas=sistema["alumnos"][codalumno]["notas"]
    notaporingresar=int(input("ingrese la nota por asignar:"))
    sistema["alumnos"][codalumno]["notas"]={"python":[notaporingresar]}
    print(sistema)
else:
    print("alumno no existe")