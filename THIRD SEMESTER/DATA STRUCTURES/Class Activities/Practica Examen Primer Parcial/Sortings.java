public class Sortings {

    public static <E extends Comparable<E>> E[] bubbleSort(E[] arreglo) {
        for (int i = 0; i < arreglo.length; i++) {
            for (int j = 0; j < arreglo.length - i; j++) {
                if (arreglo[i].compareTo(arreglo[j]) < 0)
            }
        }
    }
}