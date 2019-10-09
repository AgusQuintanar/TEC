import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import javax.swing.JFrame;

/*******************************************
 * Agustin Salvador Quintanar de la Mora   *
 * A01636142                               *
 * Clase: YaMeHizeBolas.java               *
 ******************************************/

 public class YaMeHiceBolas extends JFrame{

    private int nivel,
                x1, 
                y1, 
                largo;
    
    public YaMeHiceBolas() {
        super("Ya me hize bolas");
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setPreferredSize(new Dimension(720,700));									;
        this.pack();
        this.nivel = 6;
        this.x1 = 50;
        this.y1 = 350;
        this.largo = 600;
        this.setVisible(true);
       
    }
    
    public void paint(Graphics g) {
        super.paint(g);
        this.pintaCirculos(g, this.nivel, this.x1, this.y1, this.largo);
    }

    public void pintaCirculos(Graphics g , int nivel , int x1 , int y1 , int largo) {

        if (nivel == 0){ //Caso base
            g.drawOval(x1, y1-(largo/2), largo, largo);
        } 
        else {
            this.pintaCirculos(g, nivel-1, x1, y1, largo);
            this.pintaCirculos(g, nivel-1, x1, y1, largo/2);
            this.pintaCirculos(g, nivel-1, x1+largo/2, y1, largo/2);
        }
    }



    public static void main(String[] args) {
        YaMeHiceBolas ymhb = new YaMeHiceBolas();
        
    }
 }