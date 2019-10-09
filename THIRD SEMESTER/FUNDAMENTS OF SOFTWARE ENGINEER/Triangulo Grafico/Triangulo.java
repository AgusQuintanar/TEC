import java.awt.Dimension;
import javafx.geometry.Point2D;
import java.awt.Color;
import java.awt.geom.Line2D;
import java.awt.Graphics2D;
import javax.swing.JPanel;
import java.awt.Graphics;

public class Triangulo extends JPanel {
    //Vertices
    private Point2D v1, 
                    v2,
                    v3;
    public Triangulo(double xV1, double yV1, double xV2, double yV2, double xV3, double yV3) {
        super();
        this.setPreferredSize(new Dimension(600,600));
        this.v1 = new Point2D(xV1, yV1);
        this.v2 = new Point2D(xV2, yV2);
        this.v3 = new Point2D(xV3, yV3);
    }

    public Double calcularArea() { //Metodo para calcular el area de un triangulo mediante producto cruz
        return Math.abs(0.5 * (((this.v2.getX()-this.v1.getX())*(this.v3.getY()-this.v1.getY())) - ((this.v3.getX()-this.v1.getX())*(this.v2.getY()-
        this.v1.getY()))));
    }

    public void paintComponent(Graphics g){
        super.paintComponent(g);
        g.setColor(Color.RED);
        Graphics2D g2 = (Graphics2D) g;
        g2.draw(new Line2D.Double(this.v1.getX(), this.v1.getY(), this.v2.getX(), this.v2.getY()));
        g2.draw(new Line2D.Double(this.v1.getX(), this.v1.getY(), this.v3.getX(), this.v3.getY()));
        g2.draw(new Line2D.Double(this.v3.getX(), this.v3.getY(), this.v2.getX(), this.v2.getY()));
    }

    public void setV1(Point2D v1){
        this.v1 = v1;
    }
    public void setV2(Point2D v2){
        this.v2 = v2;
    }
    public void setV3(Point2D v3){
        this.v3 = v3;
    }
    public Point2D getV1(){
        return this.v1;
    }
    public Point2D getV2(){
        return this.v2;
    }
    public Point2D getV3(){
        return this.v3;
    }
}