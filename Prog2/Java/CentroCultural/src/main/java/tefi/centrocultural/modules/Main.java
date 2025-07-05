package tefi.centrocultural.modules;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import tefi.centrocultural.classes.Artista;
import tefi.centrocultural.classes.Exposicion;

public class Main {
    public static void main(){
        Scanner scanner = new Scanner(System.in);
        
        Map<Integer, Artista> artistas = new HashMap<>();
        Map<Integer, Exposicion> exposiciones = new HashMap<>();
        
        ArrayList<String> disciplinas = new ArrayList<>();
        ArrayList<String> artistasL = new ArrayList<>();
        ArrayList<String> expoL = new ArrayList<>();
        
        Map<Artista, Integer> cantE = new HashMap();
        // ----
        disciplinas.add("Escritura");
        disciplinas.add("Pintura");
        disciplinas.add("Fotografía");
        // ----
        System.out.println("--- Gestión ---");
        System.out.println("1- Registrar");
        System.out.println("2- Asignar");
        System.out.println("3- Informe disciplinas");
        
        System.out.println("Opcion: ");
        int opcion = scanner.nextInt();
        
        if (opcion == 1){
            System.out.println("\n1- Nuevo artista");
            System.out.println("2- Nueva disciplina");
            System.out.println("3- Nueva exposicion");
            
            System.out.println("Opción: ");
            int opcion2 = scanner.nextInt();
            
            if (opcion2 == 1){
                Op1_1.op1_1(artistas, disciplinas, artistasL);
            }
            
            if (opcion2 == 2){
                Op1_2.op2_2(disciplinas);
            }
            
            if (opcion2 == 3){
                Op1_3.op1_3(exposiciones, expoL);
            }   
        }
        
        if (opcion == 2){
            Op2.op2(artistasL, expoL, cantE);
        }
        
        if (opcion == 3){
            Op3.op3(cantE, disciplinas);
        }
        
    }
}
