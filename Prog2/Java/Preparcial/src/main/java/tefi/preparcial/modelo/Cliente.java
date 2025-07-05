package tefi.preparcial.modelo;

public class Cliente {
    int dni;
    String nombre;
    String tel;
    String mail;

    public Cliente() {
    }

    public Cliente(int dni, String nombre, String tel, String mail) {
        this.dni = dni;
        this.nombre = nombre;
        this.tel = tel;
        this.mail = mail;
    }

    public int getDni() {
        return dni;
    }

    public String getNombre() {
        return nombre;
    }

    public String getTel() {
        return tel;
    }

    public String getMail() {
        return mail;
    }

    public void setDni(int dni) {
        this.dni = dni;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setTel(String tel) {
        this.tel = tel;
    }

    public void setMail(String mail) {
        this.mail = mail;
    }
}
