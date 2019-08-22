import java.awt.Point;

import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;

import java.awt.Graphics;
import java.awt.Dimension;
import java.awt.Color;


public class SierpinskiGasket extends JFrame{
    private Point a,
                  b,
                  c;
    private int nivel;

    public SierpinskiGasket() {
        super("Fractal Sierpinski Gasket");
        this.setSize(640, 420);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.a = new Point(320, 50);
        this.b = new Point(20,380);
        this.c = new Point(620,380);
        JPanel p1 = new JPanel();
        p1.setSize(new Dimension(200,400));
        p1.setBackground(Color.BLUE);
        this.add(new JPanel());
        this.nivel = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el nivel de profundidad: "));
        this.setVisible(true);
    }

    public Point puntoMedio(Point a, Point b) {
        int pmX = (a.x + b.x)/2,
            pmY = (a.y + b.y)/2;
        return new Point(pmX,pmY);
    }

    public void paintComponent(Graphics g) {
        g.setColor(Color.RED);
        g.fillRect(30, 30, 300, 300);
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
        }
        else {
            Point pmAB = this.puntoMedio(a,b),
                  pmAC = this.puntoMedio(a,c),
                  pmBC = this.puntoMedio(b,c);

            this.pintaTriangulos(g, nivel, a, pmAB, pmBC);
            this.pintaTriangulos(g, nivel, pmAB, b, pmBC);
            this.pintaTriangulos(g, nivel, pmAC, pmBC, c);

        }
    }

    public static void main(String[] args) {
        SierpinskiGasket sg = new SierpinskiGasket();
    
        
    }
}