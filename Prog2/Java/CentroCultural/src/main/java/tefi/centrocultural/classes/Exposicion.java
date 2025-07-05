package tefi.centrocultural.classes;

public class Exposicion {
    private int codE;
    private String nombre;
    private String tematica;

    public Exposicion(int codE, String nombre, String tematica) {
        this.codE = codE;
        this.nombre = nombre;
        this.tematica = tematica;
    }

    public int getCodE() {
        return codE;
    }

    public String getNombre() {
        return nombre;
    }

    public String getTematica() {
        return tematica;
    }

    public void setCodE(int codE) {
        this.codE = codE;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setTematica(String tematica) {
        this.tematica = tematica;
    }
}
