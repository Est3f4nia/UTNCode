package tefi.ac7;

import java.sql.*;
import java.util.*;
import java.io.File;
import java.io.IOException;
import com.fasterxml.jackson.databind.ObjectMapper;
import tefi.ac7.modules.Categoria;
import tefi.ac7.modules.Producto;

public class AC7 {

    public static void main(String[] args) {
        ObjectMapper om = new ObjectMapper();
        
        try{
            // 1: conexión a base de datos
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/inventario", "root", "root");
            System.out.println("[*] Conectando...");
            Statement stmt = con.createStatement();
            // 2: comprobación de que no haya ejecución previa -> tablas creadas previamente
            try{
                File file = new File("C:\\Users\\Usuario\\OneDrive\\Documentos\\NetBeansProjects\\AC7\\src\\main\\java\\tefi\\ac7\\files\\comp.json");
                Map<String, Object> comp = om.readValue(file, Map.class);
                
                if ((Boolean) comp.get("empty")){
                    System.out.println("[*] Creando tabla: categorias");
                    stmt.executeUpdate("CREATE TABLE categorias(id int NOT NULL PRIMARY KEY AUTO_INCREMENT, nombre varchar(50) NOT NULL);");
                    
                    System.out.println("[*] Creando tabla: productos");
                    stmt.executeUpdate("CREATE TABLE productos(id int NOT NULL PRIMARY KEY AUTO_INCREMENT, nombre varchar(50) NOT NULL, precio decimal(13, 3) NOT NULL, categoria int NOT NULL REFERENCES categorias (id) ON DELETE CASCADE);");
                    
                    comp.put("empty", false);
                    om.writeValue(file, comp);
                }
  
            } catch (IOException e){
                e.printStackTrace();
            }

            // 3: suponiendo que el usuario ingrese manualmente los valores. Creación de categorías y productos como objetos, inserción de los mismos
            Categoria cat1 = new Categoria(1, "Alimentos");
            String sqlcat1 = "INSERT INTO categorias (id, nombre) VALUES (?, ?)";
            try (PreparedStatement ps = con.prepareStatement(sqlcat1)) {
                ps.setInt(1, cat1.getId());
                ps.setString(2, cat1.getNombre());
                ps.executeUpdate();
            }

            Categoria cat2 = new Categoria(2, "Cosmética");
            String sqlcat2 = "INSERT INTO categorias (id, nombre) VALUES (?, ?)";
            try (PreparedStatement ps = con.prepareStatement(sqlcat2)) {
                ps.setInt(1, cat2.getId());
                ps.setString(2, cat2.getNombre());
                ps.executeUpdate();
            }

            Categoria cat3 = new Categoria(3, "Varios");
            String sqlcat3 = "INSERT INTO categorias (id, nombre) VALUES (?, ?)";
            try (PreparedStatement ps = con.prepareStatement(sqlcat3)) {
                ps.setInt(1, cat3.getId());
                ps.setString(2, cat3.getNombre());
                ps.executeUpdate();
            }

            Producto pr1 = new Producto(1, "Manzana", 5.0, cat1);
            String sqlpr1 = "INSERT INTO productos (id, nombre, precio, categoria) VALUES (?, ?, ?, ?)";
            try (PreparedStatement ps = con.prepareStatement(sqlpr1)) {
                ps.setInt(1, pr1.getId());
                ps.setString(2, pr1.getNombre());
                ps.setDouble(3, pr1.getPrecio());
                ps.setObject(4, pr1.getCategoria().getId());
                ps.executeUpdate();
            }

            Producto pr2 = new Producto(2, "Gloss Cereza", 45.0, cat2);
            String sqlpr2 = "INSERT INTO productos (id, nombre, precio, categoria) VALUES (?, ?, ?, ?)";
            try (PreparedStatement ps = con.prepareStatement(sqlpr2)) {
                ps.setInt(1, pr2.getId());
                ps.setString(2, pr2.getNombre());
                ps.setDouble(3, pr2.getPrecio());
                ps.setObject(4, pr2.getCategoria().getId());
                ps.executeUpdate();
            }

            Producto pr3 = new Producto(3, "Cereal", 15.00, cat1);
            String sqlpr3 = "INSERT INTO productos (id, nombre, precio, categoria) VALUES (?, ?, ?, ?)";
            try (PreparedStatement ps = con.prepareStatement(sqlpr3)) {
                ps.setInt(1, pr3.getId());
                ps.setString(2, pr3.getNombre());
                ps.setDouble(3, pr3.getPrecio());
                ps.setObject(4, pr3.getCategoria().getId());
                ps.executeUpdate();
            }

            Producto pr4 = new Producto(4, "Tijera Oficina", 20.0, cat3);
            String sqlpr4 = "INSERT INTO productos (id, nombre, precio, categoria) VALUES (?, ?, ?, ?)";
            try (PreparedStatement ps = con.prepareStatement(sqlpr4)) {
                ps.setInt(1, pr4.getId());
                ps.setString(2, pr4.getNombre());
                ps.setDouble(3, pr4.getPrecio());
                ps.setObject(4, pr4.getCategoria().getId());
                ps.executeUpdate();
            }

            Producto pr5 = new Producto(5, "Post-it", 10.5, cat3);
            String sqlpr5 = "INSERT INTO productos (id, nombre, precio, categoria) VALUES (?, ?, ?, ?)";
            try (PreparedStatement ps = con.prepareStatement(sqlpr5)) {
                ps.setInt(1, pr5.getId());
                ps.setString(2, pr5.getNombre());
                ps.setDouble(3, pr5.getPrecio());
                ps.setObject(4, pr5.getCategoria().getId());
                ps.executeUpdate();
            }
            
            // 4: ejecución y salida de consulta
            
            ResultSet rs = stmt.executeQuery("select nombre, categoria from productos;");
            while(rs.next()){
                System.out.println(rs.getString(1) + " " + rs.getInt(2) + " ");
            }
            
            con.close();

        } catch(Exception e){ 
            System.out.println(e);
        }
    }

}
