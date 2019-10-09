/*******************************************
 * Agustin Salvador Quintanar de la Mora   *
 * A01636142                               *
 * Clase: Calculadora.java                 *
 ******************************************/

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import javax.swing.JFrame;
import javax.swing.JPanel;
import java.awt.BorderLayout;

public class VentanaCalculadora extends JFrame {

    private int ancho,
                alto;

    public VentanaCalculadora() {
        super("Calculadora by Agus Quintanar 1.0");

        this.ancho = 750;
        this.alto = (int) (this.ancho * .6);
        LCD lcd = new LCD(ancho, alto);
        Calculadora calculadora = new Calculadora(lcd);
        this.add(lcd, BorderLayout.NORTH);
        this.add(new PanelOperadoresAvanzados(ancho, alto, calculadora), BorderLayout.WEST);
        this.add(new PanelOperadoresBasicos(ancho, alto, calculadora), BorderLayout.EAST);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.pack();
        this.setVisible(true);
    }

    public static void main(String[] args) {
        VentanaCalculadora calculadora = new VentanaCalculadora();
    }
}





