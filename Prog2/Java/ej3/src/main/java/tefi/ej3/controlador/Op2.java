package tefi.ej3.controlador;

import java.util.List;
import java.util.Scanner;
import java.util.HashSet;
import java.util.Set;
import tefi.ej3.modelo.Libro;
import tefi.ej3.vista.Libreria;

public class Op2 {
    public static void consultaAutor(List<Libro> libros, List<String> autores){
        Scanner sc = new Scanner(System.in);
        
        System.out.println("\n--- Buscar por autor ---");
        System.out.println("Autores cargados en el sistema:");
        Set<String> autoresUnicos = new HashSet<>(autores); // evitar autores repetidos
        int i = 1;
        for (String autor : autoresUnicos) {
            System.out.println(i + "- " + autor);
            i++;
        }
        
        System.out.println("> Opcion: ");
        int opcion = sc.nextInt();
        String autorSeleccionado = (String) autoresUnicos.toArray()[opcion - 1]; // convierte el hashset en una lista String y selecciona el autor dado
        
        int totalLibros = 0;
        for (Libro libro : libros){
            if (libro.getAutor().equals(autorSeleccionado)) {
                totalLibros = totalLibros + 1;
                System.out.println(libro.getTitulo());
            }
        }
        System.out.println("Total de libros para el autor/a " + autorSeleccionado + ": " + totalLibros);
        Libreria.menu();
    }
}
