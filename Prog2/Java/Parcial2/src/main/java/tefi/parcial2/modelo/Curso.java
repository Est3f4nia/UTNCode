package tefi.parcial2.modelo;

public class Curso {
    int idCurso;
    String nombre;
    double duracion;
    int idProfesor;
    int maxAlumnos;

    public Curso() {
    }

    public Curso(int idCurso, String nombre, double duracion, int idProfesor, int maxAlumnos) {
        this.idCurso = idCurso;
        this.nombre = nombre;
        this.duracion = duracion;
        this.idProfesor = idProfesor;
        this.maxAlumnos = maxAlumnos;
    }

    public int getIdCurso() {
        return idCurso;
    }

    public String getNombre() {
        return nombre;
    }

    public double isDuracion() {
        return duracion;
    }

    public int getIdProfesor() {
        return idProfesor;
    }

    public int getMaxAlumnos() {
        return maxAlumnos;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setDuracion(double duracion) {
        this.duracion = duracion;
    }

    public void setIdProfesor(int idProfesor) {
        this.idProfesor = idProfesor;
    }

    public void setMaxAlumnos(int maxAlumnos) {
        this.maxAlumnos = maxAlumnos;
    }

    public void setIdCurso(int idCurso) {
        this.idCurso = idCurso;
    }
}
