package tefi.parcial2.controlador;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.io.File;
import java.io.IOException;

public class Comprobar {
    public static boolean comprobarCurso(int idC){
        ObjectMapper om = new ObjectMapper();
        File file = new File("C:\\Users\\Usuario\\OneDrive\\Documentos\\NetBeansProjects\\Parcial2\\src\\main\\java\\tefi\\parcial2\\modelo\\cursos.json");
        try {
            if (file.exists()) {
                JsonNode db = om.readTree(file);
                
                if(db.isArray()){
                    for (JsonNode curso : db){
                        if (curso.get("idCurso").asInt() == idC){
                            return true;
                        }
                    }
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
            return false;
        } 
        return false;
    }
    
    
    
}
