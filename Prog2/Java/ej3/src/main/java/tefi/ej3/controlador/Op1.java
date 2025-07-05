package tefi.ej3.controlador;

import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;
import tefi.ej3.vista.Libreria;
import java.io.File;
import java.io.IOException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.JsonNode;

import tefi.ej3.modelo.Libro;

public class Op1 {
    public static void nuevoLibro(List libros, List autores, List ilustradores){
        Scanner sc = new Scanner(System.in);
        ObjectMapper om = new ObjectMapper();
        File file = new File("C:\\Users\\Usuario\\Documentos\\TUP\\Programación II\\Java\\Practicas\\GuiaU42\\ej3\\src\\main\\java\\tefi\\ej3\\archivo\\allBooks.json");
        
        System.out.println("\n--- Nuevo libro ---");
        
        System.out.println("ID:");
        int id = sc.nextInt(); 
        sc.nextLine();
        
        System.out.println("Titulo: ");
        String titulo = sc.nextLine();
        sc.nextLine();
        
        System.out.println("Autor: ");
        String autor = sc.nextLine();
        sc.nextLine();
        
        System.out.println("Ilustrador: ");
        String ilustrador = sc.nextLine();
        sc.nextLine();
        
        System.out.println("Genero: ");
        String genero = sc.nextLine();
        sc.nextLine();
        
        System.out.println("Reseña: ");
        String resenia = sc.nextLine();
        sc.nextLine();
        
        Libro newLibro = new Libro(id, titulo, autor, ilustrador, genero, resenia);
        JsonNode librojson = om.valueToTree(newLibro); // formatea objeto a JSON

        try {
            List<JsonNode> line = new ArrayList<>();
            if (file.exists()) { // comprueba la existencia del archivo especificado
                JsonNode dbLibros = om.readTree(file); // lee el archivo completo
                if (dbLibros.isArray()) { 
                    for (JsonNode lib : dbLibros) { // para los libros dentro del archivo
                        line.add(lib); // añade libros
                    }
                }
            }

            line.add(librojson); // a la variable del archivo, añade la nueva linea
            om.writerWithDefaultPrettyPrinter().writeValue(file, line);
        } catch (IOException e) {
            e.printStackTrace();
        }
                
        libros.add(newLibro);
        autores.add(autor);
        ilustradores.add(ilustrador);
        
        System.out.println("[*] Libro creado");
        Libreria.menu();
    }
}
