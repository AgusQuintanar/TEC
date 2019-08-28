/*******************************************
 * Agustin Salvador Quintanar de la Mora   *
 * A01636142                               *
 * Clase: BusquedaBinaria.java             *
 ******************************************/

public class BusquedaBinaria {

    public static <E extends Comparable<E>> int binarySearchRec(E[] valores,E valor) {
       return binarySearchRec(valores, valor, 0, valores.length-1);
    }

    private static <E extends Comparable<E>> int binarySearchRec(E[] valores,E valor,int min,int max) {
        int avg = (min + max) / 2;
        if (min > max) return -1;
        else if (valores[avg].equals(valor)) return avg;
        else {    
            if (valor.compareTo(valores[avg])<0) max = avg - 1;
            else min = avg + 1;
            return binarySearchRec(valores, valor, min, max);
        }      
    }

}