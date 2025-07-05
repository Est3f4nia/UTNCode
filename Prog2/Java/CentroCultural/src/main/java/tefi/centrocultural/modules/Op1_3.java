package tefi.centrocultural.modules;

import java.util.*;
import tefi.centrocultural.classes.Exposicion;

public class Op1_3 {
    public static void op1_3(Map exposiciones, ArrayList expoL){
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("ID:");
        int codE = scanner.nextInt();
        
        scanner.nextLine();
        
        System.out.println("\nNombre:");
        String nombre = scanner.nextLine(); 
        
        System.out.println("\nTemática:");
        String tematica = scanner.nextLine(); 
        
        Exposicion expo = new Exposicion(codE, nombre, tematica);
        exposiciones.put(codE, expo);
        expoL.add(nombre);
        
        Main.main();
    }
}
