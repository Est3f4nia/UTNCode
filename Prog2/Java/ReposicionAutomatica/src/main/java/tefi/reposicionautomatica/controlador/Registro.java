package tefi.reposicionautomatica.controlador;

import java.util.List;

import tefi.reposicionautomatica.modelo.Articulo;

public class Registro {
    public static boolean tipo(List<String> tipos, String nombre){
        tipos.add(nombre);
        return true;
    }
    
    public static boolean articulo(List<Articulo> articulos, int cod, String nombre, String tipo, int stock, int stockMin, int stockMax){
        Articulo art = new Articulo(cod, nombre, tipo, stock, stockMin, stockMax);
        articulos.add(art);
        return true;
    }
    
}
