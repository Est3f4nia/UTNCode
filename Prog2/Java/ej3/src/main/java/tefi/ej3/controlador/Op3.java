package tefi.ej3.controlador;

import java.util.HashSet;
import java.util.List;
import java.util.Scanner;
import java.util.Set;
import tefi.ej3.modelo.Libro;
import tefi.ej3.vista.Libreria;

public class Op3 {
    public static void consultaIlustrador(List<Libro> libros, List<String> ilustradores){
        Scanner sc = new Scanner(System.in);
        
        System.out.println("\n--- Buscar por ilustrador ---");
        System.out.println("Ilustradores cargados en el sistema:");
        Set<String> ilusUnicos = new HashSet<>(ilustradores);
        int i = 1;
        for (String ilustrador : ilusUnicos) {
            System.out.println(i + "- " + ilustrador);
            i++;
        }
        
        System.out.println("> Opcion: ");
        int opcion = sc.nextInt();
        String ilustradorSeleccionado = (String) ilusUnicos.toArray()[opcion - 1];
        
        int totalLibros = 0;
        for (Libro libro : libros){
            if (libro.getIlustrador().equals(ilustradorSeleccionado)) {
                totalLibros = totalLibros + 1;
                System.out.println(libro.getTitulo());
            }
        }
        
        System.out.println("Total de libros para el ilustrador/a " + ilustradorSeleccionado + ": " + totalLibros);
        Libreria.menu();
    }
}
