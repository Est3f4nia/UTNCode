package tefi.parcial2.modelo;

public class Alumno {
    int dni;
    String nombre;
    int idCurso;
    //Curso curso; // o int idCurso -> agregar id a la clase curso

    public Alumno() {
    }

    public Alumno(int dni, String nombre, int idCurso) {
        this.dni = dni;
        this.nombre = nombre;
        this.idCurso = idCurso;
        //this.curso = curso;
    }

    public int getDni() {
        return dni;
    }

    public String getNombre() {
        return nombre;
    }

    //public Curso getCurso() {
    //    return curso;}

    public int getIdCurso() {
        return idCurso;
    }

    public void setDni(int dni) {
        this.dni = dni;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    //public void setCurso(Curso curso) {this.curso = curso;}
}
