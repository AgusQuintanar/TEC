/*******************************************
 * Agustin Salvador Quintanar de la Mora   *
 * A01636142                               *
 * Clase: Ordenamientos.java               *
 ******************************************/
import java.util.Random; 
public class Ordenamientos {

    public static <E extends Comparable<E>> void bubbleSort(E[] datos) { //Bubble Sort
        boolean ordenados = false;
        int indice = 1;
        while (!ordenados){
            ordenados = true;
            for (int i=0; i < datos.length - indice; i++){
                if (datos[i+1].compareTo(datos[i])<0) {
                    swap(datos, i, i+1);
                    ordenados = false;
                } 
            }
            indice += 1;
        }        
    }

    public static <E extends Comparable<E>> void mergesort(E[] datos, int ini, int fin) {
        if (ini<fin) {
            int mid = (ini+fin)/2;
            mergesort(datos, ini, mid);
            mergesort(datos, mid + 1, fin);
            merge(datos,ini,fin);
        }
    }

    public static <E extends Comparable<E>> void mergesort(E[] datos) {
        mergesort(datos, 0, datos.length - 1);
    }

    public static <E extends Comparable<E>> void merge(E[] datos, int ini, int fin) {
        E[] datosTemp = (E[])new Comparable[fin-ini+1];
    
        int mid = (ini+fin)/2,
            i = ini,
            j = mid+1,
            k = 0;
            
		while (i <= mid && j <= fin) {
		    if (datos[i].compareTo(datos[j])<=0) datosTemp[k] = datos[i++];
		    else datosTemp[k] = datos[j++];
            k++;
        }
        
		if (i <= mid && j > fin) { //Llena por la izquierda
		    while (i <= mid) datosTemp[k++] = datos[i++];
		} else { //Llena  por la derecha
		    while (j <= fin) datosTemp[k++] = datos[j++];
		}

        for (int l = 0; l < datosTemp.length; l++) {
            datos[ini+l] = datosTemp[l];
        }
    }

    public static <E> void swap(E[] lista, int x, int y) {
        E temp = lista[x];
        lista[x] = lista[y];
        lista[y] = temp;
    }

    public static <E> void imprimeArreglo(E[] arreglo) {
        for (E valor:arreglo) System.out.print(valor+",");
        System.out.println();
    }

    public static <E extends Comparable <E>> void quicksort(E[] datos) {
        quicksort(datos,0,datos.length-1);
    }

    private static <E extends Comparable <E>> void quicksort(E[] datos, int left, int right) {
        if (left < right) {
            int p = particionar(datos, left, right);
            quicksort(datos,left,p-1);
            quicksort(datos, p+1, right);
        }
    }

    private static <E extends Comparable <E>>int particionar(E[] datos, int left, int right) {
        E pivote = datos[left];
        int i = left + 1;
		for(int j = left+1; j<=right; j++) {
			if (datos[j].compareTo(pivote)<0) {
				swap(datos,i,j);
				i++;
            }
        }
        swap(datos,left,i-1);
		return i-1;
    }
    public static void main(String[] args) {
       
    }
}
