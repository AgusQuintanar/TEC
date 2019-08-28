import java.awt.Point;

import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;

import java.awt.Graphics;
import java.awt.Dimension;
import java.awt.Color;


public class ACL extends JFrame{
    private Point a,
                  b,
                  c;
    private int nivel;

    public ACL() {
        super("Fractal Sierpinski Gasket");
        this.setPreferredSize(new Dimension(720,700));
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.a = new Point(320, 50);
        this.b = new Point(20,380);
        this.c = new Point(620,380);
        this.nivel = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el nivel de profundidad: "));
        this.pack();
        this.setVisible(true);
    }

    public Point puntoMedio(Point a, Point b) {
        int pmX = (a.x + b.x)/2,
            pmY = (a.y + b.y)/2;
        return new Point(pmX,pmY);
    }

    public void paint(Graphics g) {
        pintaTriangulos(g, nivel, a, b, c);
    }

    public void pintaLineas(Graphics g, Point a, Point b) {
        g.drawLine(a.x, a.y, b.x, b.y);
    }

    public void pintaTriangulos(Graphics g, int nivel, Point a, Point b, Point c) {
        if (nivel == 0){
            pintaLineas(g, a, b);
            pintaLineas(g, a, c);
            pintaLineas(g, b, c);
            g.drawOval(x1, y1-(largo/2), largo, largo);

        }
        else {
            Point pmAB = this.puntoMedio(a,b),
                  pmAC = this.puntoMedio(a,c),
                  pmBC = this.puntoMedio(b,c);

            this.pintaTriangulos(g, nivel-1, a, pmAB, pmAC);
            this.pintaTriangulos(g, nivel-1, pmAB, b, pmBC);
            this.pintaTriangulos(g, nivel-1, pmAC, pmBC, c);


        }
    }

    public static void main(String[] args) {
       ACL sg = new ACL();
    
        
    }
}