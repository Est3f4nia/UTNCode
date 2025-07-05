package tefi.recuperatorio;

import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;

import tefi.recuperatorio.modelo.*;
import tefi.recuperatorio.controlador.*;

public class Recuperatorio {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Pasajero> pasajeros = new ArrayList<>();
        List<Viaje> viajes = new ArrayList<>();
        List<Guia> guias = new ArrayList<>();
        List<ViajeA> viajesA = new ArrayList<>();

        System.out.println("----- Sistema de gestión de viajes -----");

        boolean salir = false;
        while (!salir) {
            System.out.println("\n1- Registrar guía.");
            System.out.println("2- Registrar viaje.");
            System.out.println("3- Registrar pasajero.");
            System.out.println("4- Asignar guía y pasajeros a un viaje");
            System.out.println("5- Informe de viajes programados");
            System.out.println("6- Buscar por fecha o destino");
            System.out.println("7- Informe de ocupación");
            System.out.println("0- Salir");
            System.out.print("> Opcion: ");
            String a = sc.nextLine();
            int opcion = Integer.parseInt(a);

            switch (opcion) {
                case 1:
                    System.out.println("--- Registrar guía ---");
                    System.out.print("ID: ");
                    String b = sc.nextLine();
                    int id = Integer.parseInt(b);
                    System.out.print("Nombre: ");
                    String nombreG = sc.nextLine();
                    System.out.print("Idiomas: ");
                    String idiomas = sc.nextLine();

                    boolean hguia = Registro.guia(guias, id, nombreG, idiomas);
                    if (hguia) {
                        System.out.print("\n[*] Guía registrado.");
                    } else {
                        System.out.print("\n[!] Problema al registrar.");
                    }
                    
                    break;

                case 2:
                    System.out.println("--- Registrar viaje ---");
                    System.out.print("ID: ");
                    String c = sc.nextLine();
                    int idV = Integer.parseInt(c);
                    System.out.print("Fecha (dd/mm/aa): ");
                    String fecha = sc.nextLine();
                    System.out.print("Destino: ");
                    String destino = sc.nextLine();

                    boolean gviaje = Registro.viaje(viajes, idV, fecha, destino);
                    if (gviaje) {
                        System.out.print("\n[*] Viaje registrado.");
                    } else {
                        System.out.print("\n[!] Problema al registrar.");
                    }

                    break;

                case 3:
                    System.out.println("--- Registrar pasajero ---");
                    System.out.print("DNI: ");
                    String f = sc.nextLine();
                    int dni = Integer.parseInt(f);
                    System.out.print("Nombre: ");
                    String nombreP = sc.nextLine();
                    System.out.print("Nacionalidad: ");
                    String nacionalidad = sc.nextLine();

                    boolean hpasaj = Registro.pasajero(pasajeros, dni, nombreP, nacionalidad);
                    if (hpasaj) {
                        System.out.print("\n[*] Pasajero registrado.");
                    } else {
                        System.out.print("\n[!] Problema al registrar.");
                    }

                    break;

                case 4:
                    if (!viajes.isEmpty()) {
                        System.out.println("--- Armar viaje ---");

                        System.out.println("Viaje: ");
                        for (Viaje t : viajes) {
                            System.out.println("ID: " + t.getId() + " - " + t.getDestino() + ": " + t.getFecha());
                        }

                        System.out.print("ID viaje: ");
                        String k = sc.nextLine();
                        int idVi = Integer.parseInt(k);

                        Viaje viajeselec = null;
                        int cont = 0;
                        for (Viaje t : viajes) {
                            if (t.getId() == idVi) {
                                viajeselec = viajes.get(cont);
                            }
                            cont++;
                        }

                        System.out.println("Guía: ");
                        for (Guia t : guias) {
                            System.out.println("ID: " + t.getId() + " - " + t.getNombre());
                        }
                        System.out.print("ID guía: ");
                        String d = sc.nextLine();
                        int idG = Integer.parseInt(d);

                        Guia guiaselec = null;
                        int contG = 0;
                        for (Guia t : guias) {
                            if (t.getId() == idG) {
                                guiaselec = guias.get(contG);
                            }
                            contG++;
                        }

                        System.out.println("Pasajeros: ");
                        for (Pasajero t : pasajeros) {
                            System.out.println("DNI: " + t.getDni() + " - " + t.getNombre());
                        }

                        System.out.print("Cantidad de pasajeros a añadir: ");
                        String e = sc.nextLine();
                        int cantP = Integer.parseInt(e);

                        cantP = cantP - 1;
                        int i = 0;
                        List<Pasajero> pasajerosV = new ArrayList<>();
                        while (i <= cantP) {
                            System.out.print("DNI pasajero: ");
                            String g = sc.nextLine();
                            int dniP = Integer.parseInt(g);

                            Pasajero ps = null;
                            int contP = 0;
                            for (Pasajero t : pasajeros) {
                                if (t.getDni() == dniP) {
                                    ps = pasajeros.get(contP);
                                    pasajerosV.add(ps);
                                }
                                contG++;
                            }
                            i++;
                        }

                        boolean hV = Asociar.armarViaje(viajesA, viajeselec, guiaselec, pasajeros);
                        if (hV) {
                            System.out.print("\n[*] Viaje armado.");
                        } else {
                            System.out.print("\n[!] Problema al registrar.");
                        }
                    } else {
                        System.out.print("\n[!] No hay viajes registrados.");
                    }

                    break;

                case 5:
                    System.out.println("--- Viajes programados ---");
                    for (ViajeA t : viajesA) {
                        System.out.println("---");
                        System.out.println("ID: " + t.getId());
                        System.out.println("Destino: " + t.getDestino() + " | " + t.getFecha());
                        System.out.println("Guía: " + t.getGuia().getId() + " - " + t.getGuia().getNombre());
                        System.out.println("Cantidad de pasajeros: " + t.getPasajeros().size());

                    }

                    break;

                case 6:
                    System.out.println("--- Búsqueda ---");
                    System.out.println("1- Fecha");
                    System.out.println("2- Destino");
                    System.out.print("> Opcion: ");
                    String x = sc.nextLine();
                    int opcionB = Integer.parseInt(x);

                    switch (opcionB) {
                        case 1: // como usé dos lista van a haber viajes duplicados
                            System.out.print("Fecha (dd/mm/aa): ");
                            String fechaV = sc.nextLine();

                            for (Viaje v : viajes) {
                                if (v.getFecha().equals(fechaV)) {
                                    System.out.println("---");
                                    System.out.println("ID: " + v.getId());
                                    System.out.println("Destino: " + v.getDestino() + " | " + v.getFecha());
                                }
                            }

                            for (ViajeA v : viajesA) {
                                if (v.getFecha().equals(fechaV)) {
                                    System.out.println("---");
                                    System.out.println("ID: " + v.getId());
                                    System.out.println("Destino: " + v.getDestino() + " | " + v.getFecha());
                                }
                            }

                            break;

                        case 2:
                            System.out.print("Destino: ");
                            String destinoV = sc.nextLine();

                            for (Viaje v : viajes) {
                                if (v.getDestino().equals(destinoV)) {
                                    System.out.println("---");
                                    System.out.println("ID: " + v.getId());
                                    System.out.println("Destino: " + v.getDestino() + " | " + v.getFecha());
                                }
                            }

                            for (ViajeA v : viajesA) {
                                if (v.getDestino().equals(destinoV)) {
                                    System.out.println("---");
                                    System.out.println("ID: " + v.getId());
                                    System.out.println("Destino: " + v.getDestino() + " | " + v.getFecha());
                                }
                            }

                            break;

                        default:
                            System.out.print("\n[!] Opción no válida.");
                            break;
                    }

                    break;

                case 7:
                    System.out.println("--- Ocupación de viajes ---");
                    for (ViajeA t : viajesA) {
                        System.out.println("---");
                        System.out.println("ID: " + t.getId());
                        System.out.println("Guía: " + t.getGuia().getId() + " - " + t.getGuia().getNombre());
                        System.out.println("Cantidad de pasajeros: " + t.getPasajeros().size());

                    }
                    System.out.println("\n");
                    for (Viaje t : viajes) {
                        System.out.println("---");
                        System.out.println("ID: " + t.getId());
                        System.out.println("Guía: no asignado");
                        System.out.println("Cantidad de pasajeros: 0");

                    }

                    break;

                case 0:
                    System.out.print("\n[*] Saliendo...");
                    salir = true;
                    break;

                default:
                    System.out.print("\n[!] Opción no válida.");
                    break;
            }
        }
    }
}
