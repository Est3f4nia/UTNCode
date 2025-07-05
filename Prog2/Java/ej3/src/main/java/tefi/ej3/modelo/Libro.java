package tefi.ej3.modelo;

public class Libro {
    private int id;
    private String titulo;
    private String autor;
    private String ilustrador;
    private String genero;
    private String resenia;

    public Libro() {
    }

    public Libro(int id, String titulo, String autor, String ilustrador, String genero, String resenia) {
        this.id = id;
        this.titulo = titulo;
        this.autor = autor;
        this.ilustrador = ilustrador;
        this.genero = genero;
        this.resenia = resenia;
    }

    public int getId() {
        return id;
    }

    public String getTitulo() {
        return titulo;
    }

    public String getAutor() {
        return autor;
    }

    public String getIlustrador() {
        return ilustrador;
    }

    public String getGenero() {
        return genero;
    }

    public String getResenia() {
        return resenia;
    }

    public void setId(int id) {
        this.id = id;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public void setAutor(String autor) {
        this.autor = autor;
    }

    public void setIlustrador(String ilustrador) {
        this.ilustrador = ilustrador;
    }

    public void setGenero(String genero) {
        this.genero = genero;
    }

    public void setResenia(String resenia) {
        this.resenia = resenia;
    }
}
