package tefi.reposicionautomatica;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import tefi.reposicionautomatica.controlador.Registro;
import tefi.reposicionautomatica.controlador.Listar;
import tefi.reposicionautomatica.modelo.Articulo;

public class ReposicionAutomatica {

    public static void main(String[] args) {
        List<String> tipos = new ArrayList<>();
        List<Articulo> articulos = new ArrayList<>();

        System.out.println("----- Stock automático -----");

        boolean salir = false;
        while (!salir) {
            Scanner sc = new Scanner(System.in);

            System.out.println("\n1- Registrar tipo de artículo.");
            System.out.println("2- Registrar artículo.");
            System.out.println("3- Listar artículos y tipos de artículo.");
            System.out.println("4- Listar por tipo de artículo (stock por debajo del mínimo).");
            System.out.println("5- Listar total de stock (menor a mayor cantidad).");
            System.out.println("6- Informe detallado de un artículo.");
            System.out.println("0- Salir.");

            System.out.print("> Opción: ");
            String a = sc.nextLine();
            int opcion = Integer.parseInt(a);

            switch (opcion) {
                case 1:
                    System.out.println("\n--- Nuevo tipo de artículo ---");
                    System.out.print("Nombre: ");
                    String nombre = sc.nextLine();

                    boolean rTipo = Registro.tipo(tipos, nombre);
                    if (rTipo) {
                        System.out.println("\n[*] Tipo de producto añadido.");
                    } else {
                        System.out.println("\n[!] Problema al añadir el tipo de artículo.");
                    }

                    break;

                case 2:
                    System.out.println("\n--- Nuevo artículo ---");
                    System.out.print("Código: ");
                    String c = sc.nextLine();
                    int cod = Integer.parseInt(c);
                    System.out.print("Nombre: ");
                    String nombreA = sc.nextLine();

                    System.out.println("Tipo: ");
                    int in = 1;
                    for (String t : tipos) {
                        System.out.print("ID: " + in + " - " + t + "\n");
                        in++;
                    }
                    System.out.print("\nID: ");
                    String d = sc.nextLine();
                    int e = Integer.parseInt(d);
                    String tipo = tipos.get(e - 1);

                    System.out.print("Stock actual: ");
                    String f = sc.nextLine();
                    int stock = Integer.parseInt(f);
                    System.out.print("Stock mínimo: ");
                    String g = sc.nextLine();
                    int stockMin = Integer.parseInt(g);
                    System.out.print("Stock máximo: ");
                    String h = sc.nextLine();
                    int stockMax = Integer.parseInt(h);

                    boolean rArt = Registro.articulo(articulos, cod, nombreA, tipo, stock, stockMin, stockMax);
                    if (rArt) {
                        System.out.println("\n[*] Artículo añadido.");
                    } else {
                        System.out.println("\n[!] Problema al añadir el artículo.");
                    }

                    break;

                case 3:
                    System.out.println("\n--- Tipos de artículos ---");
                    int ind = 1;
                    for (String t : tipos) {
                        System.out.print("ID: " + ind + " - " + t + "\n");
                        ind++;
                    }

                    System.out.println("\n--- Artículos ---");
                    for (Articulo t : articulos) {
                        System.out.println("---");
                        System.out.println("Código: " + t.getCod());
                        System.out.println("Nombre: " + t.getNombre());
                        System.out.println("Tipo: " + t.getTipo());
                        System.out.println("Stock: " + t.getStock());
                        System.out.println("Stock mínimo: " + t.getStockMin());
                        System.out.println("Stock máximo: " + t.getStockMax());
                    }

                    break;

                case 4:
                    System.out.println("\n--- Listar por tipo ---");
                    System.out.println("Tipos de artículos: ");
                    int inde = 1;
                    for (String t : tipos) {
                        System.out.print("\nID: " + inde + " - " + t);
                        inde++;
                    }
                    System.out.print("\nID: ");
                    String i = sc.nextLine();
                    int j = Integer.parseInt(i);
                    String tipoA = tipos.get(j - 1);

                    for (Articulo t : articulos) {
                        if (t.getTipo().equals(tipoA)) {
                            System.out.println(t.toString());
                        }
                    }

                    break;

                case 5:
                    List<Articulo> artOrdenados = new ArrayList<>(Listar.porStock(articulos));
                    System.out.println("\n--- Artículos ordenados por cantidad de stock ---");
                    for (Articulo t : artOrdenados) {
                        System.out.println("---");
                        System.out.println("Código: " + t.getCod());
                        System.out.println("Nombre: " + t.getNombre());
                        System.out.println("Tipo: " + t.getTipo());
                        System.out.println("Stock: " + t.getStock());
                        System.out.println("Stock mínimo: " + t.getStockMin());
                        System.out.println("Stock máximo: " + t.getStockMax());
                    }

                    break;

                case 6:
                    System.out.println("\n--- Detalle de artículo ---");
                    System.out.print("ID: ");
                    String m = sc.nextLine();
                    int n = Integer.parseInt(m);

                    for (Articulo t : articulos) {
                        if (t.getCod() == n) {
                            System.out.println("---");
                            System.out.println("Código: " + t.getCod());
                            System.out.println("Nombre: " + t.getNombre());
                            System.out.println("Tipo: " + t.getTipo());
                            System.out.println("Stock: " + t.getStock());
                            System.out.println("Stock mínimo: " + t.getStockMin());
                            System.out.println("Stock máximo: " + t.getStockMax());
                        }
                    }

                    break;

                case 0:
                    salir = true;
                    System.out.println("\n[*] Saliendo...");
                    break;
                
                default:
                    System.out.println("\n[!] Opción no válida.");
                    break;
            }
        }
    }
}
