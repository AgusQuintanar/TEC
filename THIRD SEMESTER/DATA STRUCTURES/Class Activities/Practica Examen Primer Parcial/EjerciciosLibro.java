public class EjerciciosLibro {


    public static void estrellas1(int n) {
        String[] estrellas = new String[n*2];
        estrellas = estrellas1(n, estrellas,0);
        for (String renglon: estrellas) System.out.println(renglon); 
    }

    public static String[] estrellas1(int n, String[] estrellas, int dir) {
        if (n == 0) {
            return estrellas;
        }else {
            estrellas[estrellas.length/2 - n + dir*(estrellas.length/2)] = estrellas[estrellas.length/2 + n - dir*(estrellas.length/2) - 1] = renglon(n);
            return estrellas1(n-1, estrellas,dir);
        }
    }

    public static void estrellas2(int n) {
        String[] estrellas = new String[n*2];
        estrellas = estrellas1(n, estrellas, 1);
        for (String renglon: estrellas) System.out.println(renglon); 
    }

    public static String renglon(int n) {
        return (n==1) ? "*" : "* " + renglon(n-1);
    }

    public static void main(String[] args) {
        estrellas1(4);
        System.out.println("--------------------------");
        estrellas2(4);
    }
}