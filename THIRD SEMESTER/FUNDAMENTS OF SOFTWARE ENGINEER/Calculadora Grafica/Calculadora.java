public class Calculadora {
    private Double resultado;
    private String displayValue;
    private LCD lcd;
    private boolean operadorInsertado;
    
    public Calculadora(LCD lcd) {
        this.resultado = 0.0;
        this.lcd = lcd;
        this.displayValue = "";
        this.operadorInsertado = false;
    }

    private boolean isNumeric(String s){
        try {
            Double.parseDouble(s);
            return true;
        } catch(NumberFormatException | NullPointerException e) {
            return false;
        }
    }
    
    public void calcular(String val) {
        this.displayValue = lcd.getDisplayValue();
        
        String[] display = this.displayValue.split(" ");

        if (this.displayValue == "0"){
            this.displayValue = "";
            this.operadorInsertado = false;
        } 
        
        if (val == "AC") {
            this.displayValue = "0";
        }

        else if (val == "="){
            String[] reales,
                     imaginarios;
            try {
                if (display[1].equals("+")) this.displayValue = Double.toString(Double.parseDouble(display[0]) + Double.parseDouble(display[2]));
                else if (display[1].equals("-")) this.displayValue = Double.toString(Double.parseDouble(display[0]) - Double.parseDouble(display[2]));
                else if (display[1].equals("/")) this.displayValue = Double.toString(Double.parseDouble(display[0]) / Double.parseDouble(display[2]));
                else if (display[1].equals("X")) this.displayValue = Double.toString(Double.parseDouble(display[0]) * Double.parseDouble(display[2]));
            } catch(NumberFormatException e) {
                System.out.println("Error");
            }
        }

        else if (isNumeric(val) || val == ".") {
            this.displayValue += val; 
        }

        else if (!isNumeric(val)){
            if (!operadorInsertado && display.length > 0) {
                this.displayValue += " " + val + " ";
                this.operadorInsertado = true;
            } 
        }
        
        this.lcd.setDisplayValue(this.displayValue);
        this.lcd.repaint();

     
    }
}