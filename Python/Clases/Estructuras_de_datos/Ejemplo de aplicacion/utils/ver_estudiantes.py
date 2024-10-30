
def consultar_estudiante(alumnos):
    nombre_a_buscar = input("Nombre que desea buscar: ")
    
    for alumno in alumnos:
        if alumno["nombre"] == nombre_a_buscar:
            alumno_encontrado = alumno
    
    print("El alumno", alumno_encontrado["nombre"], "tiene una edad de", alumno_encontrado["edad"], "y sus calificaciones son:", alumno_encontrado["calificacion_1"], alumno_encontrado["calificacion_2"], alumno_encontrado["calificacion_3"])

def ordenar_estudiante(alumnos):
    max = 0
    for alumno in alumnos:
        if alumno["edad"] > max:
            max = alumno["edad"]
    print("La maxima edad es:", max)
        

def listar_estudiante(alumnos):
    print("Listado de alumnos:")
    for alumno in alumnos:
        print("El alumno", alumno["nombre"], "tiene una edad de", alumno["edad"], "y sus calificaciones son:", alumno["calificacion_1"], alumno["calificacion_2"], alumno["calificacion_3"])
    print("----------")