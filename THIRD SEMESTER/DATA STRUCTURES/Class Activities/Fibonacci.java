public class Fibonacci {

    public static long calcularFibonacci(int n) {
        if (n <= 1) return 1;
        else return calcularFibonacci(n-1) + calcularFibonacci(n-2);
    }

    public static long calcularFibonacciOpt(int n){
        long[] tabla = new long[n+1];
        tabla[0] = tabla[1] = 1;
        return calcularFibonacciOpt(n, tabla);
    }

    public static long calcularFibonacciOpt(int n, long[]  tabla) {
        
        if (tabla[n] == 1) return tabla[n];
        else {
            tabla[n] =  calcularFibonacciOpt(n-2) + calcularFibonacciOpt(n-1);
            return tabla[n]; 
        }
    }

    public static void main (String[] args) {
        System.out.println(calcularFibonacciOpt(10));
    }
}