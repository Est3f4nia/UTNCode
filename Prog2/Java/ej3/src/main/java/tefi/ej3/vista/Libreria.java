package tefi.ej3.vista;

import java.util.*;
import tefi.ej3.modelo.Libro;
import tefi.ej3.controlador.Op1;
import tefi.ej3.controlador.Op2;
import tefi.ej3.controlador.Op3;
import tefi.ej3.controlador.Op4;

public class Libreria {
    public static void menu(){
        List<Libro> libros = new ArrayList<>();
        List<String> autores = new ArrayList<>();
        List<String> ilustradores = new ArrayList<>();
        

        
        Scanner sc = new Scanner(System.in);
        
        System.out.println("--- Menu ---");
        System.out.println("1- Registrar libro");
        System.out.println("2- Consultar libros de autor");
        System.out.println("3- Consultar libros de ilustrador");
        System.out.println("4- Consultar libros de autor e ilustrador");
        System.out.println("5- Salir");
        
        
        System.out.println("> Opcion: ");
        int opcion = sc.nextInt();
        
        if (opcion == 1){
            Op1.nuevoLibro(libros, autores, ilustradores);
        }
        
        if (opcion == 2){
            Op2.consultaAutor(libros, autores);
        }
        
        if (opcion == 3){
            Op3.consultaIlustrador(libros, ilustradores);
        }
        
        if (opcion == 4){
            Op4.op4(libros, autores, ilustradores);
        }
        
        if (opcion == 5){
            System.out.println("[*] Saliendo...");
        }
    }
}
