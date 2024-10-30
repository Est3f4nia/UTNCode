from utils.modificar_estudiantes import (agregar_estudiante, eliminar_estudiante)
from utils.ver_estudiantes import (consultar_estudiante, listar_estudiante, ordenar_estudiante)

alumnos = []
opcion_menu = 0
while opcion_menu != 6:
    print("Seleccione una opción:")
    print("1. Agregar estudiante")
    print("2. Consultar datos de un estudiante")
    print("3. Eliminar estudiante")
    print("4. Obtener alumno con maxima edad")
    print("5. Listar estudiantes")
    print("6. Salir")
    opcion_menu = int(input("> "))
    
    if opcion_menu == 1:
        alumnos = agregar_estudiante(alumnos)
        print(alumnos)
    elif opcion_menu == 2:
        consultar_estudiante(alumnos)
    elif opcion_menu == 3:
        alumnos = eliminar_estudiante(alumnos)
    elif opcion_menu == 4:
        ordenar_estudiante(alumnos)
    elif opcion_menu == 5:
        listar_estudiante(alumnos)
    elif opcion_menu == 6:
        print("Se terminó el programa")