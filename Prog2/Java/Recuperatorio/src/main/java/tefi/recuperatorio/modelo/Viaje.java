package tefi.recuperatorio.modelo;

public class Viaje {
    int id;
    String fecha;
    String destino;

    public Viaje(int id, String fecha, String destino) {
        this.id = id;
        this.fecha = fecha;
        this.destino = destino;
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

    public void setId(int id) {
        this.id = id;
    }

    public void setFecha(String fecha) {
        this.fecha = fecha;
    }

    public void setDestino(String destino) {
        this.destino = destino;
    }

}
