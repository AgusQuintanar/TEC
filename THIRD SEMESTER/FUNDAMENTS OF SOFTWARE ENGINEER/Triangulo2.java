import javax.swing.JFrame;
import javax.swing.JOptionPane;

import javafx.geometry.Point2D;

/*#################################################################
#   Autor: Agustin Salvador Quintanar de la Mora                  #  
#   Matricula: A01636142                                          #  
#   Fecha de creacion: 9 de Septiembre del 2019                   #
#   Solucionador de triangulo                                     #
#################################################################*/ 

public class Triangulo extends JFrame {
    //Vertices
    private Point2D v1, 
                    v2,
                    v3; 


    public Triangulo() { //Construcor default
        this(0,0,0,0,0,0);
    }

    public Triangulo(double xV1, double yV1, double xV2, double yV2, double xV3, double yV3) { // Constructor con valores doubles
        this(new Point2D(xV1, yV1),new Point2D(xV2, yV2),new Point2D(xV3, yV3));
    } 

    public Triangulo(Point2D v1, Point2D v2, Point2D v3) { //Constructor con Puntos Doubles
        this.v1 = v1;
        this.v2 = v2;
        this.v3 = v3;
    } 

    public void calcularArea() { //Metodo para calcular el area de un triangulo mediante producto cruz
        JOptionPane.showMessageDialog(null, "El area del triangulo es de: "+ Math.abs(0.5 * (((this.v2.getX()-
        this.v1.getX())*(this.v3.getY()-this.v1.getY())) - ((this.v3.getX()-this.v1.getX())*(this.v2.getY()-
        this.v1.getY())))) + " unidades cuadradas.", "Area del triangulo", JOptionPane.INFORMATION_MESSAGE);
    }
    public static void main(String[] args) {
        Triangulo triangulo1 = new Triangulo();
        triangulo1.calcularArea();
    }

	public void setV1(Point2D point2d) {
	}

}
