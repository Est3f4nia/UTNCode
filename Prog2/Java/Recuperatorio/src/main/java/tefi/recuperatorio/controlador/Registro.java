package tefi.recuperatorio.controlador;

import java.util.List;
import tefi.recuperatorio.modelo.*;

public class Registro {
    public static boolean guia(List<Guia> guias, int id, String nombre, String idiomas){
        Guia guia = new Guia(id, nombre, idiomas);
        guias.add(guia);
        return true;
    }
    
    public static boolean pasajero(List<Pasajero> pasajeros, int dni, String nombre, String nacionalidad){
        Pasajero pasajero = new Pasajero(dni, nombre, nacionalidad);
        pasajeros.add(pasajero);
        return true;
    }
    
    public static boolean viaje(List<Viaje> viajes, int id, String fecha, String destino){
        Viaje viaje = new Viaje(id, fecha, destino);
        viajes.add(viaje);
        return true;
    }
    
}
