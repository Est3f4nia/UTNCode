package tefi.recuperatorio.controlador;

import tefi.recuperatorio.modelo.*;
import java.util.List;

public class Asociar {
    public static boolean armarViaje(List<ViajeA> viajesA, Viaje viaje, Guia guia, List<Pasajero> pasajeros){
        ViajeA viajeB = new ViajeA(viaje.getId(), viaje.getFecha(), viaje.getDestino(), guia, pasajeros);
        viajesA.add(viajeB);
        return true;
    }
}
