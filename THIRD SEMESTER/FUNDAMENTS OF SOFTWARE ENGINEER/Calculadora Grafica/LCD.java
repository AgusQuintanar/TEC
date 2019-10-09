import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import javax.swing.JFrame;
import javax.swing.JPanel;
import java.awt.BorderLayout;
import java.awt.Font;
import java.awt.FontFormatException;
import java.awt.GraphicsEnvironment;
import java.io.IOException;
import java.io.File;


public class LCD extends JPanel {
    private int ancho, 
                alto;
    private Font fuenteLCD;
    private String displayValue;
    public LCD(int ancho, int alto) {
        super();
        this.ancho = ancho;
        this.alto = (int) (1.5 * alto/ 6.5);  
        this.setPreferredSize(new Dimension(this.ancho, this.alto));
        this.setBackground(new Color(220,220,220));
        this.displayValue = "0";
        try {
            this.fuenteLCD = Font.createFont(Font.TRUETYPE_FONT, new File("LuckiestGuy-Regular.ttf")).deriveFont((float)this.alto*1f);
            GraphicsEnvironment ge = GraphicsEnvironment.getLocalGraphicsEnvironment();
            ge.registerFont(this.fuenteLCD);
       } catch (IOException|FontFormatException e) {
            System.out.println("Fuente no encontrada");
       }
    }
    
    public void setDisplayValue(String dv){
        this.displayValue = dv;
    }

    public String getDisplayValue() {
        return this.displayValue;
    }

    public void paintComponent(Graphics g){
        g.setFont(this.fuenteLCD);
        g.drawString(this.displayValue, (int)(this.ancho/52), (int)(.85*this.alto));
    }
}