package tefi.reposicionautomatica.controlador;

import java.util.List;
import java.util.ArrayList;

import tefi.reposicionautomatica.modelo.Articulo;

public class Listar {
    public static List porStock(List<Articulo> articulos){ 
        List<Articulo> articulosOrdenados = new ArrayList<>(articulos);
        articulosOrdenados.sort((a1, a2) -> Integer.compare(a1.getStock(), a2.getStock()));
        return articulosOrdenados;
    }
    
    
}
