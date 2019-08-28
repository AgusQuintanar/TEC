/*******************************************
 * Agustin Salvador Quintanar de la Mora   *
 * A01636142                               *
 * Clase: Ordenamientos.java               *
 ******************************************/

import java.util.Collection;
import java.util.Collections;

public class Ordenamientos {
    public static <E extends Comparable<E>> void bubbleSort(E[] datos) {
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

    public static <E> void swap(E[] lista, int x, int y) {
        E temp = lista[x];
        lista[x] = lista[y];
        lista[y] = temp;
    }

    public static <E> void imprimeArreglo(E[] arreglo) {
        for (E valor:arreglo) System.out.print(valor+",");
        System.out.println();
    }
}