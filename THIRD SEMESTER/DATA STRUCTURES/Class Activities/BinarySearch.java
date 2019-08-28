public class BinarySearch {
    public static int binarySearch(int valor, int[] valores) {
        int min = 0,
            max = valores.length-1,
            avg = (min + max) / 2;

            while(min <= max) {
                if (valores[avg] == valor) {
                    return avg;
                }
                else if (valor < valores[avg]) max = avg - 1;
                else min = avg + 1;
                avg = (min + max)/2;
            }

            return -1;
    }


    public static int binarySearch(String valor, String[] valores) {
        int min = 0,
            max = valores.length-1,
            avg = (min + max) / 2;

            while(min <= max) {
                if (valores[avg].equals(valor)) {
                    return avg;
                }
                else if (valor.compareTo(valores[avg])<0) max = avg - 1;
                else min = avg + 1;
                avg = (min + max)/2;
            }

            return -1;
    }


    public static <E extends Comparable<E>> int binarySearch(E valor, E[] valores) {
        int min = 0,
            max = valores.length-1,
            avg = (min + max) / 2;

            while(min <= max) {
                if (valores[avg].equals(valor)) {
                    return avg;
                }
                else if (valor.compareTo(valores[avg])<0) max = avg - 1;
                else min = avg + 1;
                avg = (min + max)/2;
            }

            return -1;
    }

    public static void main(String[] args) {
        int[] arr = {1,2,3,4,5,6,7,8,9,10};
        System.out.println(binarySearch(7, arr));
    }
}