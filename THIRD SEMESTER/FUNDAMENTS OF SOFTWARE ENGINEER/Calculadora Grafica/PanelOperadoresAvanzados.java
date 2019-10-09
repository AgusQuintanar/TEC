import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import javax.swing.JFrame;
import javax.swing.JPanel;
import java.awt.BorderLayout;

public class PanelOperadoresAvanzados extends JPanel{
    private int ancho, 
                alto;
    private Calculadora calculadora;
    public PanelOperadoresAvanzados(int ancho, int alto, Calculadora calculadora) {
        super();
        this.ancho = (int) (3 * ancho/ 8);
        this.alto = (int) (5 * alto/ 6.5);
        this.calculadora = calculadora;  
        this.setPreferredSize(new Dimension(this.ancho, this.alto));
        this.setBackground(new Color(30,30,30));
    } 
}