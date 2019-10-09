import java.awt.Dimension;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JButton;
import javax.swing.JPanel;
import javax.swing.JTextField;

import javafx.geometry.Point2D;

public class PanelControl extends JPanel{
    private JTextField  tfV1x,
                        tfV1y,
                        tfV2x,
                        tfV2y,
                        tfV3x,
                        tfV3y,
                        tfArea;
    private Triangulo triangulo;
    
private JButton btnDibujarTriangulo,
                btnCalcularArea;


public PanelControl() {
    super();
    this.setPreferredSize(new Dimension(200,600));

    this.triangulo = new Triangulo(200,600,600,600,400,200);

    this.tfV1x =new JTextField(10);
    this.tfV1y =new JTextField(10);
    this.tfV2x =new JTextField(10);
    this.tfV2y =new JTextField(10);
    this.tfV3x =new JTextField(10);
    this.tfV3y =new JTextField(10);

    this.btnDibujarTriangulo = new JButton("Dibujar triangulo");
    this.btnDibujarTriangulo.addActionListener(new ActionListener(){
        @Override
        public void actionPerformed(ActionEvent e) {
            triangulo.setV1(new Point2D(Double.parseDouble(tfV1x.getText()), Double.parseDouble(tfV1y.getText())));
            triangulo.setV2(new Point2D(Double.parseDouble(tfV2x.getText()), Double.parseDouble(tfV2y.getText())));
            triangulo.setV3(new Point2D(Double.parseDouble(tfV3x.getText()), Double.parseDouble(tfV3y.getText())));
        }

    });
    
    this.btnCalcularArea = new JButton("Calcular area");
    this.btnCalcularArea.addActionListener(new ActionListener(){
        @Override
        public void actionPerformed(ActionEvent e) {
            tfArea.setText(Double.toString(calcularArea()));
        }
    });
    
    this.add(this.tfV1x);
    this.add(this.tfV1y);
    this.add(this.tfV2x);
    this.add(this.tfV2y);
    this.add(this.tfV3x);
    this.add(this.tfV3y);
    this.add(this.tfArea);
    this.add(this.btnCalcularArea);
    this.add(this.btnDibujarTriangulo);
}



}