import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.Insets;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.LineBorder;

import java.awt.BorderLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.*;
import javax.swing.*;

public class PanelOperadoresBasicos extends JPanel {
    private int ancho, 
                alto;

    private Calculadora calculadora;

    private JButton btnParentesisAbierto,
                    btnParentesisCerrado,
                    btnNegativo,
                    btnDelete,
                    btnAC,
                    btnIzquierda,
                    btnDerecha,
                    btn1,
                    btn2,
                    btn3,
                    btn4,
                    btn5,
                    btn6,
                    btn7,
                    btn8,
                    btn9,
                    btn0,
                    btnPor,
                    btnEntre,
                    btnSuma,
                    btnResta,
                    btnPunto,
                    btnImaginario,
                    btnIgual,
                    btnAns;

    public PanelOperadoresBasicos(int ancho, int alto, Calculadora calculadora) {
        super(new FlowLayout(FlowLayout.LEFT, 0, 0));
        this.ancho = (int) (5 * ancho/ 8);
        this.alto = (int) (5 * alto/ 6.5);
        this.calculadora = calculadora;  
        this.setPreferredSize(new Dimension(this.ancho, this.alto));
        this.setBackground(new Color(40,40,40));
        this.btnParentesisAbierto = new JButton("(");
        this.btnParentesisCerrado = new JButton(")");
        this.btnNegativo = new JButton("( - )");
        this.btnDelete = new JButton("DEL");
        this.btnAC = new JButton("AC");
        this.btnIzquierda = new JButton("<");
        this.btnDerecha = new JButton(">");
        this.btn1 = new JButton("1");
        this.btn2 = new JButton("2");
        this.btn3 = new JButton("3");
        this.btn4 = new JButton("4");
        this.btn5 = new JButton("5");
        this.btn6 = new JButton("6");
        this.btn7 = new JButton("7");
        this.btn8 = new JButton("8");
        this.btn9 = new JButton("9");
        this.btn0 = new JButton("0");
        this.btnPor = new JButton("X");
        this.btnEntre = new JButton("/");
        this.btnSuma = new JButton("+");
        this.btnResta = new JButton("-");
        this.btnPunto = new JButton(".");
        this.btnImaginario = new JButton("i");
        this.btnIgual = new JButton("=");
        this.btnAns = new JButton("ANS");



        JButton[] arrBotones = {this.btnParentesisAbierto,this.btnParentesisCerrado,this.btnNegativo,this.btnDelete,
                                this.btnAC,this.btn7,this.btn8,this.btn9,this.btnIzquierda,this.btnDerecha, this.btn4,
                                this.btn5,this.btn6,this.btnPor,this.btnEntre,this.btn1,this.btn2,this.btn3,this.btnSuma,
                                this.btnResta, this.btn0,this.btnPunto,this.btnImaginario,this.btnAns,this.btnIgual};

        
        
        for (JButton boton : arrBotones) {
            boton.setPreferredSize(new Dimension((int) (this.ancho/5),(int) (this.alto/5)));
            boton.setMargin(new Insets(0, 0, 0, 0));
            boton.setFont(new Font("Arial", Font.BOLD, 20));
            boton.setOpaque(true);
            boton.setBorderPainted(true);
            
            if (boton.getText() == "AC" || boton.getText() == "DEL") boton.setBackground(new Color(220,40,40));
            else if (boton.getText() == "=") boton.setBackground(new Color(255,128,40));
            else boton.setBackground(new Color(40,40,40));
            boton.setBorder(new LineBorder(new Color(60,60,60), 1));
            boton.setForeground(Color.WHITE);
            boton.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    calculadora.calcular(boton.getText());
                }
            });
            this.add(boton);
        }



    }
}