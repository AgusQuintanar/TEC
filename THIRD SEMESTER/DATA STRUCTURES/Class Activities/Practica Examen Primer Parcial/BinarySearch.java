public class BinarySearch {

    public static <E extends Comparable<E>> int binarySearch(E[] arreglo, E dato) {
        return binarySearch(arreglo, dato, 0, arreglo.length - 1);
    }

    public static <E extends Comparable<E>> int binarySearch(E[] arreglo, E dato, int min, int max) {
        int avg = (min + max)/2;
        if (min > max) return -1;
        else if (arreglo[avg].equals(dato)) return avg;
        else {
            if (dato.compareTo(arreglo[avg]) < 0) max = avg -1;
            else min = avg + 1;
            return binarySearch(arreglo, dato, min, max);
        } 
        
    }

    public static void main(String[] args) {
        Integer[] a = {1,2,3,4,5,6,7,8,9,10};
        System.out.println(binarySearch(a,5));        
    }
}