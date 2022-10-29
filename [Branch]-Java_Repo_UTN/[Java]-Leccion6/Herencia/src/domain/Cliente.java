package domain;

import java.util.Date;

/**
 * @author Aguppesce
 */
/*============CLASE 09 - VIERNES-28/10/2022============*/
public class Cliente extends Persona {

    //Atributos
    private int idCliente;
    private Date fechaRegistro;//Importar la clase Date
    private boolean vip;//Very important person
    private static int contadorClientes;//Tipo estático

    //Constructor
    public Cliente(Date fechaRegistro, boolean vip, String nombre, char genero, int edad, String direccion) {
        super(nombre, genero, edad, direccion);
        this.fechaRegistro = fechaRegistro;
        this.vip = vip;
        this.idCliente = ++Cliente.contadorClientes;
    }

    public int getIdCliente() {
        return idCliente;
    }

    public Date getFechaRegistro() {
        return fechaRegistro;
    }

    public void setFechaRegistro(Date fechaRegistro) {
        this.fechaRegistro = fechaRegistro;
    }

    public boolean isVip() {
        return vip;
    }

    public void setVip(boolean vip) {
        this.vip = vip;
    }

    @Override
    public String toString() {
        StringBuilder  sb = new StringBuilder();
        sb.append("Cliente{idCliente=").append(idCliente);
        sb.append(", fechaRegistro=").append(fechaRegistro);
        sb.append(", vip=").append(vip);
        sb.append(", ").append(super.toString());
        sb.append("}");
        return sb.toString();
    }

}

