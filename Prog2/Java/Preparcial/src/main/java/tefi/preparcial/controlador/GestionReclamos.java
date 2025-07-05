package tefi.preparcial.controlador;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ObjectNode;
import com.fasterxml.jackson.databind.node.ArrayNode;
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import tefi.preparcial.modelo.Reclamo;

public class GestionReclamos {
    
    public static boolean nuevoReclamo(int cliente, String servicio, String detalle, String fecha, String estado) {
        ObjectMapper om = new ObjectMapper();
        Reclamo re = new Reclamo(cliente, servicio, detalle, fecha, estado);
        File file = new File("C:\\Users\\Usuario\\OneDrive\\Documentos\\NetBeansProjects\\Preparcial\\src\\main\\java\\tefi\\preparcial\\modelo\\reclamos.json");
        JsonNode reclamojson = om.valueToTree(re);

        try {
            List<JsonNode> line = new ArrayList<>();
            if (file.exists()) {
                JsonNode dbReclamos = om.readTree(file);
                if (dbReclamos.isArray()) {
                    for (JsonNode o : dbReclamos) {
                        if (o.equals(reclamojson)) {
                            return false;
                        } else {
                            line.add(o);
                        }
                    }
                }
            }

            line.add(reclamojson);
            om.writerWithDefaultPrettyPrinter().writeValue(file, line);
            return true;
        } catch (IOException e) {
            e.printStackTrace();
            return false;
        }
    }
    
    public static String listarReclamos() {
        ObjectMapper om = new ObjectMapper();
        File file = new File("C:\\Users\\Usuario\\OneDrive\\Documentos\\NetBeansProjects\\Preparcial\\src\\main\\java\\tefi\\preparcial\\modelo\\reclamos.json");
        try {
            if (file.exists()) {
                JsonNode db = om.readTree(file);

                String dbReclamos = om.writerWithDefaultPrettyPrinter().writeValueAsString(db);
                return dbReclamos;
            } else {
                return "false";
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }
    
    public static int numReclamos(int dni){
        ObjectMapper om = new ObjectMapper();
        File file = new File("C:\\Users\\Usuario\\OneDrive\\Documentos\\NetBeansProjects\\Preparcial\\src\\main\\java\\tefi\\preparcial\\modelo\\reclamos.json");
        try {
            if (file.exists()) {
                JsonNode db = om.readTree(file);
                
                int cant = 0;
                if(db.isArray()){
                    for (JsonNode reclamo : db){
                        if (reclamo.get("cliente").asInt() == dni){
                            cant++;
                        }
                    }
                    return cant;
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
            return 0;
        } 
        return 0;
    }
    
    public static int estadoReclamosListarNum(int t){
        ObjectMapper om = new ObjectMapper();
        File file = new File("C:\\Users\\Usuario\\OneDrive\\Documentos\\NetBeansProjects\\Preparcial\\src\\main\\java\\tefi\\preparcial\\modelo\\reclamos.json");
        
        String tipo = "";
        if (t == 1) {
            tipo = "Registrado";
        }
        if (t == 2) {
            tipo = "Asignado";
        }
        if (t == 3) {
            tipo = "Terminado";
        }
        
        try {
            if (file.exists()) {
                JsonNode db = om.readTree(file);

                int cant = 0;
                if(db.isArray()){
                    for (JsonNode reclamo : db){
                        if (reclamo.get("estado").asText().equals(tipo)){
                            cant++;
                        }
                    }
                    return cant;
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
            return 0;
        } 
        return 0;
    }
    
    public static boolean modificarEstado(int dni, String nuevoEstado){
        ObjectMapper om = new ObjectMapper();
        File file = new File("C:\\Users\\Usuario\\OneDrive\\Documentos\\NetBeansProjects\\Preparcial\\src\\main\\java\\tefi\\preparcial\\modelo\\reclamos.json");
        
        try {
            if (file.exists()) {
                JsonNode db = om.readTree(file);

                if (db.isArray()) {
                    ArrayNode reclamosArray = (ArrayNode) db;
                    
                    for (JsonNode reclamo : db) {
                        if (reclamo.get("cliente").asInt() == dni) {
                            ObjectNode valor = (ObjectNode) reclamo;
                            valor.put("estado", nuevoEstado);
                            om.writerWithDefaultPrettyPrinter().writeValue(file, reclamosArray);
                        }
                    }
                    return true;
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
            return false;
        }
        return false;
    }
    


    
}
