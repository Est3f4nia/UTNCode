package tefi.recuperatorio.modelo;

import java.util.List;

public class ViajeA {
    int id;
    String fecha;
    String destino;
    Guia guia;
    List<Pasajero> pasajeros;

    public ViajeA(int id, String fecha, String destino, Guia guia, List<Pasajero> pasajeros) {
        this.id = id;
        this.fecha = fecha;
        this.destino = destino;
        this.guia = guia;
        this.pasajeros = pasajeros;
    }

    public int getId() {
        return id;
    }

    public String getFecha() {
        return fecha;
    }

    public String getDestino() {
        return destino;
    }

    public Guia getGuia() {
        return guia;
    }

    public List<Pasajero> getPasajeros() {
        return pasajeros;
    }

    public void setId(int id) {
        this.id = id;
    }

    public void setFecha(String fecha) {
        this.fecha = fecha;
    }

    public void setDestino(String destino) {
        this.destino = destino;
    }

    public void setGuia(Guia guia) {
        this.guia = guia;
    }

    public void setPasajeros(List<Pasajero> pasajeros) {
        this.pasajeros = pasajeros;
    }
    
    
}
