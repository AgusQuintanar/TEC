/*******************************************
 * Agustin Salvador Quintanar de la Mora   *
 * A01636142                               *
 * Clase: MyHashTable.java                 *
 ******************************************/
import java.util.LinkedList;
import java.util.NoSuchElementException;
public class MyHashTable <K extends Comparable<K>,V extends Comparable<V>> {
    private int size;
    private LinkedList<MyNodoHT<K,V>>[] tabla;
    private static final double LoadFactor = 0.75;

    public MyHashTable() {
        this.size = 0;
        this.tabla = (LinkedList<MyNodoHT<K,V>>[]) new LinkedList[11];
        for (int i=0; i < this.tabla.length; i++) {
            this.tabla[i] = new LinkedList<>();
        }
    }

    public void put(K llave, V valor) {
        if ((double)this.size / this.tabla.length > MyHashTable.LoadFactor) rehashing();
        int pos = Math.abs(llave.hashCode()%this.tabla.length);
        this.tabla[pos].add(new MyNodoHT<>(llave, valor));
        this.size++;
    }

    public V get(K llave) {
        int pos = Math.abs(llave.hashCode()%this.tabla.length);
        for (MyNodoHT<K,V> nodo:this.tabla[pos]) {
            if (llave.compareTo(nodo.llave)==0) return nodo.valor;
        }
        throw new NoSuchElementException("No se encontro esa llave.");
    }

    private void rehashing() {
        LinkedList<MyNodoHT<K,V>>[] tablaTemp = (LinkedList<MyNodoHT<K,V>>[]) new LinkedList[2*this.tabla.length+1];
        for (int i=0; i < tablaTemp.length; i++) {
            tablaTemp[i] = new LinkedList<>();
        }
        for (LinkedList<MyNodoHT<K,V>> lista : this.tabla){
            for (MyNodoHT<K,V> nodo: lista){
                int pos = Math.abs(nodo.llave.hashCode()%tablaTemp.length);
                tablaTemp[pos].add(new MyNodoHT<>(nodo.llave, nodo.valor));
            }
        }
        this.tabla = tablaTemp;
    }

    public V remove(K llave) {
        int pos = Math.abs(llave.hashCode()%this.tabla.length);
        for (MyNodoHT<K,V> nodo:this.tabla[pos]) {
            if (nodo.llave.compareTo(llave)==0) {
                V valorTemp = nodo.valor; 
                this.tabla[pos].remove(nodo);
                this.size--;
                return valorTemp;
            }
        }
        throw new NoSuchElementException("No se encontro esa llave");
    }

    public boolean containsKey(K llave){
        int pos = Math.abs(llave.hashCode()%this.tabla.length);
        for (MyNodoHT<K,V> nodo:this.tabla[pos]) {
            if (nodo.llave.compareTo(llave)==0) return true;
        }
        return false;
    }

    public void imprimirHashTable() {
        for (LinkedList<MyNodoHT<K,V>> lista : this.tabla){
            for (MyNodoHT<K,V> nodo: lista){
                System.out.println(nodo);
            }
        } 
    }

    public static void main(String[] args) {
        MyHashTable<Integer,String> ht = new MyHashTable<>();
        ht.imprimirHashTable();
        ht.put(1, "Manzana");
        ht.put(2, "Pera");
        ht.put(3, "Platano");
        ht.put(4, "Durazno");
        ht.put(5, "Sandia");
        ht.put(6, "Jicama");
        ht.put(7, "Zanahoria");
        ht.put(8, "Calabaza");
        ht.put(9, "Melon");
        ht.put(10, "Papaya");
        ht.put(11, "Tuna");
        ht.put(12, "Uva");
        ht.imprimirHashTable();
        System.out.println("Size: " + ht.size);
        System.out.println("Tamano tabla: " + ht.tabla.length);
       
        System.out.println("----------------------------------");
        // ht.remove(3);
        // ht.remove(7);
        // ht.remove(11);
        ht.imprimirHashTable();
        System.out.println("Size: " + ht.size);

        for (int i=1; i<13; i++) System.out.println(ht.get(i));
        System.out.println("----------------------------------");

        System.out.println(ht.remove(3));
        System.out.println(ht.remove(5));
        System.out.println(ht.remove(11));

        System.out.println("----------------------------------");

        for (int i=1; i<13; i++) {
            if (ht.containsKey(i)) System.out.println("true: " + i);
            else System.out.println("false: " + i);
        }

    }
}

class MyNodoHT<K,V> {
    K llave;
    V valor;

    public MyNodoHT(K llave, V valor) {
        this.llave = llave;
        this.valor = valor;
    }

    public String toString() {
        return "Key: " + this.llave + ", Value:"+this.valor;
    }
}