package tefi.recuperatorio.modelo;

public class Guia {
    int id;
    String nombre;
    String idiomas;

    public Guia(int id, String nombre, String idiomas) {
        this.id = id;
        this.nombre = nombre;
        this.idiomas = idiomas;
    }

    public int getId() {
        return id;
    }

    public String getNombre() {
        return nombre;
    }

    public String getIdiomas() {
        return idiomas;
    }

    public void setId(int id) {
        this.id = id;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setIdiomas(String idiomas) {
        this.idiomas = idiomas;
    }
}
