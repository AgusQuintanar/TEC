/*******************************************
 * Agustin Salvador Quintanar de la Mora   *
 * A01636142                               *
 * Clase: BusquedaBinaria.java             *
 ******************************************/

public class BinarySearchTareaRad {

    public static void binarySearchRec(int[][] valores,int valor) {
       binarySearchRec(valores, valor, 0, valores[0].length*valores[0].length-1);
    }

    private static void binarySearchRec(int[][] valores,int valor,int min,int max) {
        int avg = (min + max) / 2;
        if (min > max) System.out.println("No se encuentra ese dato");
        else if (valores[avg/valores[0].length][avg%valores[0].length] == valor) System.out.println(avg/valores[0].length + ", " + avg%valores[0].length);
        else {    
            if (valor < valores[avg/valores[0].length][avg%valores[0].length]) max = avg - 1;
            else min = avg + 1;
            binarySearchRec(valores, valor, min, max);
        }      
    }

    public static void main(String[] args) {
        BinarySearchTareaRad bs = new BinarySearchTareaRad();
        int[][] a = {{1,2,3,4},{5,6,7,8},{9,10,11,12},{13,14,15,16}};
        binarySearchRec(a, 10);
    }

}