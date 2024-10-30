
def agregar_estudiante(alumnos):
    nombre = input("Ingrese nombre: ")
    edad = int(input("ingrese edad: "))
    calificacion_1 = float(input("ingrese c1: "))
    calificacion_2 = float(input("ingrese c2: "))
    calificacion_3 = float(input("ingrese c3: "))
    
    alumnos.append({
        "nombre": nombre,
        "edad": edad,
        "calificacion_1": calificacion_1,
        "calificacion_2": calificacion_2,
        "calificacion_3": calificacion_3,
    })
    return alumnos

def eliminar_estudiante(alumnos):
    alumno_a_eliminar = input("Alumno que quiere borrar: ")
    for i in range(len(alumnos)):
        if alumnos[i]["nombre"] == alumno_a_eliminar:
            alumno_encontrado = i
    alumnos.pop(alumno_encontrado)
    return alumnos
