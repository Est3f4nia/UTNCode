package tefi.parcial2.vista;

import tefi.parcial2.controlador.Registro;

import java.util.Scanner;
import java.util.Map;
import java.util.HashMap;
import tefi.parcial2.controlador.Listado;
import tefi.parcial2.controlador.Comprobar;

public class Menu {
    public static void menu(){
        Map<Integer, Integer> cantAlumnosCurso = new HashMap<>();
        
        Scanner sc = new Scanner(System.in);
        
        System.out.println("\n----- Gestión de cursos -----");
        System.out.println("1- Nuevo alumno.");
        System.out.println("2- Nuevo docente.");
        System.out.println("3- Nuevo curso.");
        System.out.println("4- Listado de cursos.");
        System.out.println("5- Alumnos inscriptos en un curso.");
        System.out.println("6- Información de alumno"); //en qué curso está inscripto, el nombre del docente a cargo y la duración del curso.
        System.out.println("7- Procentaje de ocupación de un curso");
        // Generar un informe por curso, que muestre el porcentaje de ocupación (cantidad actual de
        //inscriptos dividido por la capacidad máxima, expresado en porcentaje).

        
        System.out.println("0- Salir");
        
        System.out.println("Opción:");
        String op = sc.nextLine();
        int opcion = Integer.parseInt(op);
        
        if (opcion == 0){
            System.out.println("[!] Saliendo del programa...\n");
        }
        
        if (opcion == 1){
            System.out.println("\n--- Nuevo alumno ---");

            System.out.println("DNI:");
            String d = sc.nextLine();
            int dni = Integer.parseInt(d);

            System.out.println("Nombre completo: ");
            String nombre = sc.nextLine();
            
            System.out.println("ID curso:");
            String i = sc.nextLine();
            int idC = Integer.parseInt(i);
            
            if (Comprobar.comprobarCurso(idC)){
                cantAlumnosCurso.put(idC, +1);
                
                boolean x = Registro.nuevoAlumno(dni, nombre, idC);
                if (x) {
                    System.out.println("\n[*] Alumno registrado.");
                    Menu.menu();
                } else {
                    System.out.println("\n[!] Problema al registrar.");
                    Menu.menu();
                }
            } else {
                System.out.println("\n[!] El curso no existe.");
                Menu.menu();
            }
        }
        
        if (opcion == 2){
            System.out.println("\n--- Nuevo docente ---");

            System.out.println("DNI:");
            String d = sc.nextLine();
            int dni = Integer.parseInt(d);

            System.out.println("Nombre completo: ");
            String nombre = sc.nextLine();
            
            System.out.println("ID curso:");
            String i = sc.nextLine();
            int idC = Integer.parseInt(i);
            
            boolean x = Registro.nuevoProfesor(dni, nombre, idC);
            if (x){
                System.out.println("\n[*] Docente registrado.");
                Menu.menu();
            } else {
                System.out.println("\n[!] Problema al registrar.");
                Menu.menu();
            }
        }
        
        if (opcion == 3){
            System.out.println("\n--- Nuevo curso ---");

            System.out.println("ID:");
            String i = sc.nextLine();
            int id = Integer.parseInt(i);

            System.out.println("Nombre: ");
            String nombre = sc.nextLine();
            
            System.out.println("Duracion:");
            String d = sc.nextLine();
            double duracion = Double.parseDouble(d);
            
            System.out.println("DNI docente: ");
            String idd = sc.nextLine();
            int idD = Integer.parseInt(idd);
            
            System.out.println("Cantidad máxima de alumnos:");
            String m = sc.nextLine();
            int maxA = Integer.parseInt(m);
            
            boolean x = Registro.nuevoCurso(id, nombre, duracion, idD, maxA);
            if (x){
                System.out.println("\n[*] Curso registrado.");
                Menu.menu();
            } else {
                System.out.println("\n[!] Problema al registrar.");
                Menu.menu();
            }
        }
        
        if (opcion == 4){
            System.out.println("\n[*] Base de datos: cursos (raw).");
            String dbCursos = Listado.listarCursos();
            
            if (dbCursos == "false" || dbCursos == null){
                System.out.println("\n[!] Problema con el archivo JSON.");
                Menu.menu();
            } else {
                System.out.println(dbCursos);
                Menu.menu();
            }
        }
        
        if (opcion == 5){
            System.out.println("\n--- Listado de alumnos ---");

            System.out.println("ID curso:");
            String i = sc.nextLine();
            int id = Integer.parseInt(i);
            
            String x = Listado.alumnosEnCurso(id);
            if (x == ""){
                System.out.println("\n[!] Problema con el archivo JSON.");
                Menu.menu();
            } else {
                System.out.println(x);
                Menu.menu();
            }
            
        }
        
        if (opcion == 6){
            System.out.println("\n--- Información de alumno ---");

            System.out.println("DNI:");
            String i = sc.nextLine();
            int dni = Integer.parseInt(i);
            
            String x = Listado.listadoAlumnoDetallado(dni);
            if (x == ""){
                System.out.println("\n[!] Problema con el archivo JSON.");
                Menu.menu();
            } else {
                System.out.println(x);
                Menu.menu();
            }
            
        }
        
        if (opcion == 7){
            System.out.println("\n--- Porcentaje de ocupación ---");
            
            System.out.println("ID curso:");
            String i = sc.nextLine();
            int id = Integer.parseInt(i);
            
            Double capacidadTotal = Listado.porcentajeCurso(id, cantAlumnosCurso);
            
            if (capacidadTotal == 0){
                System.out.println("\n[!] No es posible mostrar.");
                Menu.menu();
            } else {
                System.out.println("Porcentaje: " + capacidadTotal + "%");
                Menu.menu();
            }
        
        }
        
    }
}