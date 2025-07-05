package tefi.parcial2.modelo;

public class Profesor {
    int dni;
    String nombre;
    int idCurso;
    //Curso curso; // o int idCurso -> agregar id a la clase curso

    public Profesor() {
    }

    public Profesor(int dni, String nombre, int idCurso) {
        this.dni = dni;
        this.nombre = nombre;
        this.idCurso = idCurso;
    }

    public int getDni() {
        return dni;
    }

    public String getNombre() {
        return nombre;
    }

    public int getidCurso() {
        return idCurso;
    }

    public void setDni(int dni) {
        this.dni = dni;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setidCurso(int curso) {
        this.idCurso = idCurso;
    }
}
