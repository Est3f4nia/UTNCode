package tefi.preparcial.modelo;

public class Reclamo {
    int cliente;
    String servicio;
    String detalle;
    String fecha;
    String estado;

    public Reclamo() {
    }

    public Reclamo(int cliente, String servicio, String detalle, String fecha, String estado) {
        this.cliente = cliente;
        this.servicio = servicio;
        this.detalle = detalle;
        this.fecha = fecha;
        this.estado = estado;
    }

    public int getCliente() {
        return cliente;
    }

    public String getServicio() {
        return servicio;
    }

    public String getDetalle() {
        return detalle;
    }

    public String getFecha() {
        return fecha;
    }

    public String getEstado() {
        return estado;
    }

    public void setCliente(int cliente) {
        this.cliente = cliente;
    }

    public void setServicio(String servicio) {
        this.servicio = servicio;
    }

    public void setDetalle(String detalle) {
        this.detalle = detalle;
    }

    public void setFecha(String fecha) {
        this.fecha = fecha;
    }

    public void setEstado(String estado) {
        this.estado = estado;
    }
}
