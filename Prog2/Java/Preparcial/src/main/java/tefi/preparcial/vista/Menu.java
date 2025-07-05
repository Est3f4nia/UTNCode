package tefi.preparcial.vista;

import java.util.Scanner;
import tefi.preparcial.controlador.GestionClientes;
import tefi.preparcial.controlador.GestionReclamos;

public class Menu {
    public static void menu(){
        Scanner sc = new Scanner(System.in);
        
        System.out.println("\n----- Gestión de clientes y reclamos -----");
        System.out.println("\n--- Gestión de clientes ---");
        System.out.println("1- Nuevo cliente.");
        System.out.println("2- Listar clientes.");
        System.out.println("3- Cantidad de reclamos por cliente.");
        System.out.println("\n--- Gestión de reclamos ---");
        System.out.println("4- Nuevo reclamo.");
        System.out.println("5- Listar reclamos.");
        System.out.println("6- Cantidad de reclamos por estado.");
        System.out.println("7- Modificar estado de reclamo."); // inicial registrado, asignado -> tecnico, terminado -> solucionado
        System.out.println("8- Clientes ordenados por número de reclamos");
        System.out.println("0- Salir");
        
        System.out.println("Opción:");
        String op = sc.nextLine();
        int opcion = Integer.parseInt(op);
        
        if (opcion == 0){
            System.out.println("[!] Saliendo del programa...\n");
        }
        
        if (opcion == 1){
            System.out.println("\n--- Nuevo cliente ---");

            System.out.println("DNI:");
            String d = sc.nextLine();
            int dni = Integer.parseInt(d);

            System.out.println("Nombre completo: ");
            String nombre = sc.nextLine();

            System.out.println("Teléfono: ");
            String tel = sc.nextLine();

            System.out.println("Mail: ");
            String mail = sc.nextLine();
            
            boolean x = GestionClientes.nuevoCliente(dni, nombre, tel, mail);
            if (x){
                System.out.println("\n[*] Cliente registrado.");
                Menu.menu();
            } else {
                System.out.println("\n[!] Problema al registrar.");
                Menu.menu();
            }
        }
        
        if (opcion == 2){
            System.out.println("\n[*] Base de datos raw.");
            String dbClientes = GestionClientes.listar();
            
            if (dbClientes == "false" || dbClientes == null){
                System.out.println("\n[!] Problema con el archivo JSON.");
                Menu.menu();
            } else {
                System.out.println(dbClientes);
                Menu.menu();
            }
        }
        
        if (opcion == 3){
            System.out.println("\n--- Reclamos por cliente ---");
            
            System.out.println("DNI:");
            String d = sc.nextLine();
            int dni = Integer.parseInt(d);
            
            System.out.println("Cantidad de reclamos para " + "(" + dni + "): " + GestionReclamos.numReclamos(dni));
            Menu.menu();
        }
        
        if (opcion == 4){
            System.out.println("\n--- Nuevo reclamo ---");

            System.out.println("DNI:");
            String d = sc.nextLine();
            int dni = Integer.parseInt(d);
            
            boolean cliente = GestionClientes.comprobar(dni);
            
            if (cliente){
                System.out.println("Servicio reclamado: ");
                String servicio = sc.nextLine();

                System.out.println("Detalle: ");
                String detalle = sc.nextLine();

                System.out.println("Fecha: ");
                String fecha = sc.nextLine();
           
                boolean x = GestionReclamos.nuevoReclamo(dni, servicio, detalle, fecha, "Registrado");
                if (x) {
                    System.out.println("\n[*] Reclamo registrado.");
                    Menu.menu();
                } else {
                    System.out.println("\n[!] Problema al registrar.");
                    Menu.menu();
                }
            } else {
                System.out.println("\n[!] Cliente no encontrado.");
                Menu.menu();
            }
        }
        
        if (opcion == 5){
            System.out.println("\n[*] Base de datos raw.");
            String dbReclamos = GestionReclamos.listarReclamos();
            
            if (dbReclamos == "false" || dbReclamos == null){
                System.out.println("\n[!] Problema con el archivo JSON.");
                Menu.menu();
            } else {
                System.out.println(dbReclamos);
                Menu.menu();
            }
        }
        
        if (opcion == 6){
            System.out.println("\n--- Reclamos por estado ---");
            System.out.println("1- Registrado");
            System.out.println("2- Asignado");
            System.out.println("3- Terminado");
            
            System.out.println("Opción:");
            String o = sc.nextLine();
            int o2 = Integer.parseInt(o);
            
            String tipo = "";
            if (o2 == 1) {
                tipo = "registrados";
            }
            if (o2 == 2) {
                tipo = "asignados";
            }
            if (o2 == 3) {
                tipo = "terminados";
            }
            
            System.out.println("Cantidad de reclamos para reclamos " + tipo + ": " + GestionReclamos.estadoReclamosListarNum(o2));
            Menu.menu();
        }        
        
        if (opcion == 7){
            System.out.println("\n--- Modificar estado de reclamo ---");

            System.out.println("DNI:");
            String d = sc.nextLine();
            int dni = Integer.parseInt(d);
            
            boolean cliente = GestionClientes.comprobar(dni);
            
            if (cliente){
                System.out.println("\n1- Registrado");
                System.out.println("2- Asignado");
                System.out.println("3- Terminado");

                System.out.println("Opción:");
                String y = sc.nextLine();
                int o = Integer.parseInt(y);

                String tipo = "";
                if (o == 1) {
                    tipo = "Registrado";
                }
                if (o == 2) {
                    tipo = "Asignado";
                }
                if (o == 3) {
                    tipo = "Terminado";
                }
                
                boolean o7 = GestionReclamos.modificarEstado(dni, tipo);
                
                if (o7){
                    System.out.println("\n[*] Estado modificado.");
                    Menu.menu();
                } else {
                    System.out.println("\n[!] Problema al modificar el estado.");
                    Menu.menu();
                }
            }
        }
        
        if (opcion == 8){
            System.out.println(GestionClientes.ordenarClientes());
            Menu.menu();
        }
        
    }
}
