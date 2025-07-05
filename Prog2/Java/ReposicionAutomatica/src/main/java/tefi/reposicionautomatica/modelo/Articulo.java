package tefi.reposicionautomatica.modelo;

public class Articulo {
    private int cod;
    private String nombre;
    private String tipo;
    private int stock;
    private int stockMin;
    private int stockMax;

    public Articulo(int cod, String nombre, String tipo, int stock, int stockMin, int stockMax) {
        this.cod = cod;
        this.nombre = nombre;
        this.tipo = tipo;
        this.stock = stock;
        this.stockMin = stockMin;
        this.stockMax = stockMax;
    }

    public int getCod() {
        return cod;
    }

    public String getNombre() {
        return nombre;
    }

    public String getTipo() {
        return tipo;
    }

    public int getStock() {
        return stock;
    }

    public int getStockMin() {
        return stockMin;
    }

    public int getStockMax() {
        return stockMax;
    }

    public void setCod(int cod) {
        this.cod = cod;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }

    public void setStock(int stock) {
        this.stock = stock;
    }

    public void setStockMin(int stockMin) {
        this.stockMin = stockMin;
    }

    public void setStockMax(int stockMax) {
        this.stockMax = stockMax;
    }

    @Override
    public String toString() {
        if (stock < stockMin){
            return "Articulo:\n" + "\n- Codigo = " + cod + "\n- Nombre = " + nombre + "\n- Tipo = " + tipo + "\n- Stock = " + stock + "\n- Stock Minimo = " + stockMin + "\n- Stock Maximo = " + stockMax + "\n[!] Sugerencia de reposición = " + (stockMax-stock) + " artículos.s";
        }
        return null;
    }
    
}