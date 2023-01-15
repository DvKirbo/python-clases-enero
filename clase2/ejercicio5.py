#minissistema de notas
#diccionario
sistema={
    "NombreDeInstitucion":"colegioN",
    "aulas":["python","javascript", "java"],
    "profesores":["Profesor1","profesor2"],
    "alumnos":{#diccionarios indentados
        "7553":{"nombre":"juan",
                "apellido":"rodriguez",
                "cursos":["python"]
                },
        
        "8225":{"nombre":"juan",
                "apellido":"rodriguez",
                "cursos":["python", "javascript"]
                },
        
        "7543":{"nombre":"juan",
                "apellido":"rodriguez",
                "cursos":["php"]
                }
    },
    "cursoprofesor":{
        "python":[],
        "php":[],
        "c++":[]
    }
}



print (sistema["cursoprofesor"][])

#asignar profesor cursos
profesoresactuales= sistema["profesores"]
profesorporasignar = input("que profesor es?")
if profesorporasignar in sistema["profesores"]:
    print("existe el profespr")
    cursoporasignar = input("QUe curso va a asignar el profesor?")
    if cursoporasignar in sistema["cursos"]:
        sistema["cursoprofesor"][cursoporasignar]=sistema["cursoprofesor"][cursoporasignar]
    else:
        print("no existe el curso")
else:
    print("No existe el profesor debe agregarlo")
    print(profesorporasignar,sistema["profesores"])
    profesortemp=sistema["profesores"]
    profesortemp.append(profesorporasignar)
    profesoresactuales=sistema["profesores"]
    
    #aignar nota alumno
    codalumno = input("codigo del alumno: ")
    listaalumnos=list()