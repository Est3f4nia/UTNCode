package tefi.parcial2.controlador;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.io.File;
import java.io.IOException;
import java.util.Map;

public class Listado {
    public static String listarCursos() {
        ObjectMapper om = new ObjectMapper();
        File file = new File("C:\\Users\\Usuario\\OneDrive\\Documentos\\NetBeansProjects\\Parcial2\\src\\main\\java\\tefi\\parcial2\\modelo\\cursos.json");
        try {
            if (file.exists()) {
                JsonNode db = om.readTree(file);

                String dbCursos = om.writerWithDefaultPrettyPrinter().writeValueAsString(db);
                return dbCursos;
            } else {
                return "false";
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }
    
    public static String alumnosEnCurso(int idC){
        ObjectMapper om = new ObjectMapper();
        File file = new File("C:\\Users\\Usuario\\OneDrive\\Documentos\\NetBeansProjects\\Parcial2\\src\\main\\java\\tefi\\parcial2\\modelo\\alumnos.json");
        try {
            if (file.exists()) {
                JsonNode db = om.readTree(file);
                String dbAlumnosC = "";
                
                if(db.isArray()){
                    for (JsonNode alumno : db){
                        if (alumno.get("idCurso").asInt() == idC){
                            dbAlumnosC += om.writerWithDefaultPrettyPrinter().writeValueAsString(alumno.get("nombre"));
                        }
                    }
                    return dbAlumnosC;
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
            return "";
        } 
        return "";
    }
    
    public static String listadoAlumnoDetallado(int dni){
        ObjectMapper om = new ObjectMapper();
        File file = new File("C:\\Users\\Usuario\\OneDrive\\Documentos\\NetBeansProjects\\Parcial2\\src\\main\\java\\tefi\\parcial2\\modelo\\alumnos.json");
        File cursos = new File("C:\\Users\\Usuario\\OneDrive\\Documentos\\NetBeansProjects\\Parcial2\\src\\main\\java\\tefi\\parcial2\\modelo\\cursos.json");
        File profesores = new File("C:\\Users\\Usuario\\OneDrive\\Documentos\\NetBeansProjects\\Parcial2\\src\\main\\java\\tefi\\parcial2\\modelo\\profesores.json");
        try {
            if (file.exists()) {
                JsonNode db = om.readTree(file);
                String dataAlumno = "";
                
                if(db.isArray()){
                    
                    JsonNode cursoAlumno;
                    for (JsonNode alumno : db){
                        if (alumno.get("dni").asInt() == dni){
                            cursoAlumno = alumno.get("idCurso");
                            
                            if (cursos.exists()) {
                                JsonNode dbCursos = om.readTree(cursos);

                                if(dbCursos.isArray()){
                                    for(JsonNode curso : dbCursos){
                                        if (curso.get("idCurso") == cursoAlumno){
                                            dataAlumno += om.writerWithDefaultPrettyPrinter().writeValueAsString(curso.get("nombre"));
                                            dataAlumno += om.writerWithDefaultPrettyPrinter().writeValueAsString(curso.get("duracion"));
                                        }   
                                    }
                                }
                            }
                            
                            if (profesores.exists()) {
                                JsonNode dbProfesores = om.readTree(profesores);

                                if(dbProfesores.isArray()){
                                    for(JsonNode profesor : dbProfesores){
                                        if (profesor.get("idCurso") == cursoAlumno){
                                            dataAlumno += om.writerWithDefaultPrettyPrinter().writeValueAsString(profesor.get("nombre"));
                                        }   
                                    }
                                }
                            }
                        }
                    }
                    return dataAlumno;
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
            return "";
        } 
        return "";
    }
    
    public static double porcentajeCurso(int idC, Map<Integer, Integer> cantAlumnos) {
        ObjectMapper om = new ObjectMapper();
        File file = new File("C:\\Users\\Usuario\\OneDrive\\Documentos\\NetBeansProjects\\Parcial2\\src\\main\\java\\tefi\\parcial2\\modelo\\cursos.json");
        try {
            if (file.exists()) {
                JsonNode db = om.readTree(file);
                
                if(db.isArray()){
                    Double capacidad = 0.0;
                    for (JsonNode curso : db){
                        if (curso.get("idCurso").asInt() == idC){
                            capacidad = curso.get("duracion").asDouble();
                        }
                    }

                    int totalA = cantAlumnos.get(idC);
                    
                    double total = totalA * 100;
                    total = total / capacidad;
                    return total;
                }
            } else {
                return 0.0;
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return 0.0;
    }
    
    
    
}
