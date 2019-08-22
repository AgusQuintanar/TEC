public class BinarySearch {
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

    public static void main(String[] args) {
        String[] arr = {"Juan","Joel","Jp","Jyan"};
        System.out.println(binarySearch("Jp", arr));
    }
}