package tefi.centrocultural.modules;

import java.util.*;

public class Op1_2 {
    public static void op2_2(ArrayList disciplinas){
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("\nNueva disciplina:");
        String disciplina = scanner.nextLine(); 
        
        disciplinas.add(disciplina);
        
        Main.main();
    }
}
