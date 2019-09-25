import javax.swing.JFrame;

import javafx.geometry.Point2D;

/*#################################################################
#   Autor: Agustin Salvador Quintanar de la Mora                  #  
#   Matricula: A01636142                                          #  
#   Fecha de creacion: 9 de Septiembre del 2019                   #
#   Solucionador de triangulo                                     #
#################################################################*/ 

public class TrianguloGrafico extends JFrame {
    //Vertices
    private Point2D v1, 
                    v2,
                    v3; 

    public TrianguloGrafico(double xV1, double yV1, double xV2, double yV2, double xV3, double yV3) { //Constructor con Puntos Doubles
        super("Triangulo grafico");
        this.setDefaultCloseOperation();
        this.v1 = new Point2D(xV1, yV1);
        this.v2 = new Point2D(xV2, yV2);
        this.v3 = new Point2D(xV3, yV3);
    } 

    public Double calcularArea() { //Metodo para calcular el area de un triangulo mediante producto cruz
        return Math.abs(0.5 * (((this.v2.getX()-this.v1.getX())*(this.v3.getY()-this.v1.getY())) - ((this.v3.getX()-this.v1.getX())*(this.v2.getY()-
        this.v1.getY()))));
    }


    public static void main(String[] args) {
        
    }
}
