/*******************************************
 * Agustin Salvador Quintanar de la Mora   *
 * A01636142                               *
 * Clase: Recursividad.java                *
 ******************************************/

 public class Recursividad {

    public static int multiplicacion(int a, int b) { //Metodo de multiplicacion con funcion auxiliar
        return sumatoria(Math.abs(a), Math.abs(b))*Integer.signum(a)*Integer.signum(b);
    }

    public static int sumatoria(int a, int b) { //Funcion auxiliar para el metodo de multiplicacion
        return (a <= 1)? b:(b + sumatoria(a-1, b));
    }

    public static int multiplicacion2(int a, int b) { //Metodo de multiplicacion sin funcion auxiliar
        return (Math.abs(a) == 1)? Math.abs(b):(Math.abs(b)+multiplicacion2(Math.abs(a)-1,Math.abs(b)))*Integer.signum(a)*Integer.signum(b);
    }

    public static String base10a2(int n) { //Metodo para convertir enteros base 10 a binario
        return (n<=1)?Integer.toString(n%2):base10a2(n/2)+ n%2;
    }

    public static void main(String[] args) {
        System.out.println(multiplicacion(-56, 5));
    }
 }