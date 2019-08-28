import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;

import javax.swing.JPanel;

public class BolasPanel extends JPanel {
	
	public BolasPanel() {
		super();
		this.setPreferredSize(new Dimension(700,720));
		//this.setBackground(Color.WHITE);
		this.setVisible(true);
		this.repaint();
	}
	
    public void pintaCirculos(Graphics g , int nivel , int x1 , int y1 , int largo) {

    }

    public void paintComponent(Graphics g) {
    	super.paintComponent(g);
        g.setColor(Color.RED);
        g.fillRect(50, 50, 800, 200);
        System.out.println("pinto");
    }
}
