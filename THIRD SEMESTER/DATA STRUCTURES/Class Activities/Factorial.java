public class Factorial {

    public static long calcular_factorial(int n) {
        if (n <= 1) return 1;
        else return n * calcular_factorial(n-1);
    }
    public static void main (String[] args){
        System.out.println(calcular_factorial(5));
    }
}