package tefi.centrocultural.modules;

import java.util.*;

public class Op2 {
    public static void op2(ArrayList artistas, ArrayList expo, Map cantArt){
        Scanner scanner = new Scanner(System.in);
        
        System.out.print(artistas);
            
        System.out.println("Seleccione un artista (nombre): ");
        String a = scanner.nextLine();
        
        String artista = "";
        for (Object b : artistas){
            if (a == b){
                artista = a;
            } else {
                System.out.println("[!] Artista no encontrado.");
            }
        }
    
        System.out.print(expo);
        
        System.out.println("Seleccione una exposicion (nombre): ");
        String c = scanner.nextLine();
        
        String exposicion = "";
        for (Object d : expo){
            if (c == d){
                exposicion = c;
                
            } else {
                System.out.println("[!] Exposicion no encontrada.");
            }
        }
        
        cantArt.put(artista, exposicion);
        Main.main();
    }
}
