package tefi.ej3.controlador;

import java.util.HashSet;
import java.util.List;
import java.util.Scanner;
import java.util.Set;
import tefi.ej3.modelo.Libro;
import tefi.ej3.vista.Libreria;

public class Op4 {
    public static void op4(List<Libro> libros, List<String> autores, List<String> ilustradores){
        Scanner sc = new Scanner(System.in);
        
        System.out.println("\n--- Buscar por autor e ilustrador ---");
        System.out.println("Autores cargados en el sistema:");
        Set<String> autoresUnicos = new HashSet<>(autores); // evitar autores repetidos
        int i = 1;
        for (String autor : autoresUnicos) {
            System.out.println(i + "- " + autor);
            i++;
        }
        
        System.out.println("> Opcion: ");
        int opcion = sc.nextInt();
        String autorSeleccionado = (String) autoresUnicos.toArray()[opcion - 1];
        
        System.out.println("\n--- Buscar por ilustrador ---");
        System.out.println("Ilustradores cargados en el sistema:");
        Set<String> ilusUnicos = new HashSet<>(ilustradores);
        int j = 1;
        for (String ilustrador : ilusUnicos) {
            System.out.println(j + "- " + ilustrador);
            j++;
        }
        
        System.out.println("> Opcion: ");
        int opcion2 = sc.nextInt();
        String ilustradorSeleccionado = (String) ilusUnicos.toArray()[opcion2 - 1];
        
        int totalLibros = 0;
        for (Libro libro : libros){
            if (libro.getIlustrador().equals(ilustradorSeleccionado) && libro.getAutor().equals(autorSeleccionado)) {
                totalLibros = totalLibros + 1;
                System.out.println(libro.getTitulo());
            }
        }
        
        System.out.println("Total de libros para el autor/a " + autorSeleccionado + " y el ilustrador/a " + ilustradorSeleccionado + ": " + totalLibros);
        Libreria.menu();
    }
}
