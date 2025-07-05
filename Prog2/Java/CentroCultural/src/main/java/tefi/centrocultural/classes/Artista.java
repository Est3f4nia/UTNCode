package tefi.centrocultural.classes;

public class Artista {
    private int codA;
    private String nombre;
    private Object disciplina;
    
    public Artista(int codA, String nombre, Object disciplina) {
        this.codA = codA;
        this.nombre = nombre;
        this.disciplina = disciplina;
    }

    public int getCodA() {
        return codA;
    }

    public String getNombre() {
        return nombre;
    }

    public Object getDisciplina() {
        return disciplina;
    }

    public void setCodA(int codA) {
        this.codA = codA;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setDisciplina(Object disciplina) {
        this.disciplina = disciplina;
    }

}
