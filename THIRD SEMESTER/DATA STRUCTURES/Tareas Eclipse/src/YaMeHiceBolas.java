import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;

import javax.swing.JFrame;
import javax.swing.JPanel;

/*******************************************
 * Agustin Salvador Quintanar de la Mora   *
 * A01636142                               *
 * Clase: YaMeHizeBolas.java               *
 ******************************************/

 public class YaMeHiceBolas extends JFrame{
    
    public YaMeHiceBolas() {
        super("Ya me hize bolas");
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setPreferredSize(new Dimension(720,700));									;
       
        this.pack();
        this.setVisible(true);
        System.out.println("step");
    }
    
    public void paint(Graphics g) {
    	super.paint(g);
    	g.drawOval(40, 40, 400, 400);
    }


    public static void main(String[] args) {
        YaMeHiceBolas ymhb = new YaMeHiceBolas();
        
    }
 }