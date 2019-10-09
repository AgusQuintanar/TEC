import javax.swing.JFrame;
import javafx.geometry.Point2D;
import java.awt.BorderLayout;

/*#################################################################
#   Autor: Agustin Salvador Quintanar de la Mora                  #  
#   Matricula: A01636142                                          #  
#   Fecha de creacion: 25 de Septiembre del 2019                  #
#   Solucionador de triangulo grafico                             #
#################################################################*/ 

public class VentanaTriangulo extends JFrame {


    public VentanaTriangulo() { //Constructor con Puntos Doubles
        super("Triangulo grafico");
		this.setDefaultCloseOperation(EXIT_ON_CLOSE);
		PanelDibujo pd=new PanelDibujo();
		this.add(pd);
		this.add(new PanelControles(pd),BorderLayout.WEST);
		this.pack();
		this.setVisible(true);

		
    }
    public static void main(String[] args) {
        VentanaTriangulo trianguloPrueba = new VentanaTriangulo();
    }
}
