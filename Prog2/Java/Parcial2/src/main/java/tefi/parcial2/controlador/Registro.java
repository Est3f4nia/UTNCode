package tefi.parcial2.controlador;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import tefi.parcial2.modelo.Alumno;
import tefi.parcial2.modelo.Curso;
import tefi.parcial2.modelo.Profesor;

public class Registro {
    public static boolean nuevoAlumno(int dni, String nombre, int idCurso){
        ObjectMapper om = new ObjectMapper();
        Alumno cl = new Alumno(dni, nombre, idCurso);
        File file = new File("C:\\Users\\Usuario\\OneDrive\\Documentos\\NetBeansProjects\\Parcial2\\src\\main\\java\\tefi\\parcial2\\modelo\\alumnos.json");
        JsonNode alumnojson = om.valueToTree(cl);

        try {
            List<JsonNode> line = new ArrayList<>();
            if (file.exists()) {
                JsonNode dbAlumnos = om.readTree(file);
                if (dbAlumnos.isArray()) { 
                    for (JsonNode o : dbAlumnos) {
                        if(o.equals(alumnojson)){
                            return false;
                        } else {
                            line.add(o);
                        }
                    }
                }
            }

            line.add(alumnojson);
            om.writerWithDefaultPrettyPrinter().writeValue(file, line);
            return true;
        } catch (IOException e) {
            e.printStackTrace();
            return false;
        }
    
    }
    
    public static boolean nuevoProfesor(int dni, String nombre, int idCurso){
        ObjectMapper om = new ObjectMapper();
        Profesor cl = new Profesor(dni, nombre, idCurso);
        File file = new File("C:\\Users\\Usuario\\OneDrive\\Documentos\\NetBeansProjects\\Parcial2\\src\\main\\java\\tefi\\parcial2\\modelo\\profesores.json");
        JsonNode profesorjson = om.valueToTree(cl);

        try {
            List<JsonNode> line = new ArrayList<>();
            if (file.exists()) {
                JsonNode dbProfesores = om.readTree(file);
                if (dbProfesores.isArray()) { 
                    for (JsonNode o : dbProfesores) {
                        if(o.equals(profesorjson)){
                            return false;
                        } else {
                            line.add(o);
                        }
                    }
                }
            }

            line.add(profesorjson);
            om.writerWithDefaultPrettyPrinter().writeValue(file, line);
            return true;
        } catch (IOException e) {
            e.printStackTrace();
            return false;
        }
    
    }
    
    public static boolean nuevoCurso(int id, String nombre, double duracion, int idProfesor, int maxAlumnos){
        ObjectMapper om = new ObjectMapper();
        Curso curso = new Curso(id, nombre, duracion, idProfesor, maxAlumnos);
        File file = new File("C:\\Users\\Usuario\\OneDrive\\Documentos\\NetBeansProjects\\Parcial2\\src\\main\\java\\tefi\\parcial2\\modelo\\cursos.json");
        JsonNode cursojson = om.valueToTree(curso);
        
        //no añade duración del curso al archivo (????
        
        try {
            List<JsonNode> line = new ArrayList<>();
            if (file.exists()) {
                JsonNode dbCursos = om.readTree(file);
                if (dbCursos.isArray()) { 
                    for (JsonNode o : dbCursos) {
                        if(o.equals(cursojson)){
                            return false;
                        } else {
                            line.add(o);
                        }
                    }
                }
            }

            line.add(cursojson);
            om.writerWithDefaultPrettyPrinter().writeValue(file, line);
            return true;
        } catch (IOException e) {
            e.printStackTrace();
            return false;
        }
    
    }
    
}
