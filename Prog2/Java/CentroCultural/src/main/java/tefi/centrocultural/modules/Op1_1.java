package tefi.centrocultural.modules;

import java.util.*;
import tefi.centrocultural.classes.Artista;

public class Op1_1 {
    public static void op1_1(Map artistas, ArrayList disciplinas, ArrayList artistasL){
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("ID:");
        int codA = scanner.nextInt();
        
        scanner.nextLine();
        
        System.out.println("\nNombre completo:");
        String nombre = scanner.nextLine(); 
        
        int v1 = 0;
        Object disciplina = disciplinas.get(0);
        if (disciplinas.isEmpty()){
            System.out.println("[!] La lista de disciplinas está vacía.");
        } else {
            System.out.println(disciplinas);
            
            System.out.println("Opcion: ");
            v1 = scanner.nextInt();
            disciplina = disciplinas.get(v1);
            
            }
        
        Artista artista = new Artista(codA, nombre, disciplina);
        artistas.put(codA, artista);
        artistasL.add(nombre);
        
        Main.main();
    }
}
