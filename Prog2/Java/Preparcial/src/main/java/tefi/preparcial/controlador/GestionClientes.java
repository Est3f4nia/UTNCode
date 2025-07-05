package tefi.preparcial.controlador;

import java.io.IOException;
import java.io.File;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;
import java.util.List;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.node.ObjectNode;
import tefi.preparcial.modelo.Cliente;

public class GestionClientes {
    
    public static boolean nuevoCliente(int dni, String nombre, String tel, String mail){
        ObjectMapper om = new ObjectMapper();
        Cliente cl = new Cliente(dni, nombre, tel, mail);
        File file = new File("C:\\Users\\Usuario\\OneDrive\\Documentos\\NetBeansProjects\\Preparcial\\src\\main\\java\\tefi\\preparcial\\modelo\\clientes.json");
        JsonNode clientejson = om.valueToTree(cl);

        try {
            List<JsonNode> line = new ArrayList<>();
            if (file.exists()) {
                JsonNode dbClientes = om.readTree(file);
                if (dbClientes.isArray()) { 
                    for (JsonNode o : dbClientes) {
                        if(o.equals(clientejson)){
                            return false;
                        } else {
                            line.add(o);
                        }
                    }
                }
            }

            line.add(clientejson);
            om.writerWithDefaultPrettyPrinter().writeValue(file, line);
            return true;
        } catch (IOException e) {
            e.printStackTrace();
            return false;
        }
    }
    
    public static String listar(){
        ObjectMapper om = new ObjectMapper();
        File file = new File("C:\\Users\\Usuario\\OneDrive\\Documentos\\NetBeansProjects\\Preparcial\\src\\main\\java\\tefi\\preparcial\\modelo\\clientes.json");
        try {
            if (file.exists()) {
                JsonNode db = om.readTree(file);
                
                String dbClientes = om.writerWithDefaultPrettyPrinter().writeValueAsString(db);
                return dbClientes;
            } else {
                return "false";
            }
        } catch (IOException e) {
            e.printStackTrace();
        } 
        return null;
    }
    
    public static boolean comprobar(int dni){
        ObjectMapper om = new ObjectMapper();
        File file = new File("C:\\Users\\Usuario\\OneDrive\\Documentos\\NetBeansProjects\\Preparcial\\src\\main\\java\\tefi\\preparcial\\modelo\\clientes.json");
        try {
            if (file.exists()) {
                JsonNode db = om.readTree(file);
                
                if(db.isArray()){
                    for (JsonNode cliente : db){
                        if (cliente.get("dni").asInt() == dni){
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
    
    public static List ordenarClientes() {
        ObjectMapper om = new ObjectMapper();
        File clientesFile = new File("C:\\Users\\Usuario\\OneDrive\\Documentos\\NetBeansProjects\\Preparcial\\src\\main\\java\\tefi\\preparcial\\modelo\\clientes.json");
        File reclamosFile = new File("C:\\Users\\Usuario\\OneDrive\\Documentos\\NetBeansProjects\\Preparcial\\src\\main\\java\\tefi\\preparcial\\modelo\\reclamos.json");

        try {
            JsonNode clientesNode = om.readTree(clientesFile);
            List<ObjectNode> listaClientes = new ArrayList<>();

            if (clientesNode.isArray()) {
                for (JsonNode cliente : clientesNode) {
                    listaClientes.add((ObjectNode) cliente);
                }
            }

            Map<Integer, Integer> contReclamos = new HashMap<>();
            JsonNode nodoReclamos = om.readTree(reclamosFile);

            if (nodoReclamos.isArray()) {
                for (JsonNode reclamo : nodoReclamos) {
                    int dniCliente = reclamo.get("cliente").asInt();
                    contReclamos.put(dniCliente, contReclamos.getOrDefault(dniCliente, 0) + 1);
                }
            }

            listaClientes.sort((c1, c2) -> {
                int reclamosC1 = contReclamos.getOrDefault(c1.get("dni").asInt(), 0);
                int reclamosC2 = contReclamos.getOrDefault(c2.get("dni").asInt(), 0);
                return Integer.compare(reclamosC2, reclamosC1); // Ordenar de mayor a menor
            });
            
            //  + cantidad de reclamos
            List<Map<String, Object>> resultados = new ArrayList<>();
            for (ObjectNode cliente : listaClientes) {
                Map<String, Object> clienteInfo = new HashMap<>();
                int dni = cliente.get("dni").asInt();
                String nombre = cliente.get("nombre").asText();
                int cantidadReclamos = contReclamos.getOrDefault(dni, 0);
                
                clienteInfo.put("dni", dni);
                clienteInfo.put("nombre", nombre);
                clienteInfo.put("cantidadReclamos", cantidadReclamos);
                resultados.add(clienteInfo);
                
            }
            
            return resultados; // producto + stock
            //return listaClientes; // informe detallado

        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }
    
    
    
}
