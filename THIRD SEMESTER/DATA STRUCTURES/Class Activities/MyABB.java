import java.util.NoSuchElementException;

/*******************************************
 * Agustin Salvador Quintanar de la Mora   *
 * A01636142                               *
 * Clase: MyABB.java                       *
 ******************************************/

 public class MyABB <E extends Comparable<E>> {
    private NodoABB<E> root;
    private int size;

    public MyABB() {
        super(); //Inicializa los atributos en su valor default
    }
    public E search(E value) {
        NodoABB<E> current = root; 
        while (current != null) {
            if (value.compareTo(current.value)==0) return current.value;
            else current = value.compareTo(current.value) <0 ? current.left : current.rigth;
        }
        throw new NoSuchElementException("No existe ese valor");
    }

    public void insert(E value) {
        if (this.size == 0) this.root = new NodoABB(value);
        else {
            NodoABB<E> current = root;
            while (current.left != null || current.rigth != null) {
                current = value.compareTo(current.value) <0 ? current.left : current.rigth;
            }
            if (value.compareTo(current.value) < 0) current.left = new NodoABB(value);
            else current.rigth = new NodoABB(value);
            
        }
        this.size++;
    }

    public void preorden() {
        preorden(this.root);
    }

    private void preorden(NodoABB<E> current) {
        if (current != null) {
            System.out.println(current.value+",");
            preorden(current.left);
            preorden(current.rigth);
        }
    }

    public void inorden() {
        inorden(this.root);
    }

    private void inorden(NodoABB<E> current) {
        if (current != null) {
            preorden(current.left);
            System.out.println(current.value+",");
            preorden(current.rigth);
        }
    }

    public void postorden() {
        postorden(this.root);
    }

    private void postorden(NodoABB<E> current) {
        if (current != null) {
            preorden(current.left);
            preorden(current.rigth);
            System.out.println(current.value+",");
        }
    }

    public void nivel() {

    }

    // public E remove(E value) {
        
    //     NodoABB<E> current = this.root;
    //     while(current != null && !current.value.equals(value)) {
    //         current = value.compareTo(current.value) < 0 ? current.left : current.rigth;
    //     }
    // }

    public static void main(String[] args) {
        MyABB<Integer> abb1 = new MyABB<>();
        abb1.insert(15);
        abb1.insert(3);
        abb1.insert(145);
        abb1.insert(13);
        abb1.insert(5);
        abb1.insert(11);
        abb1.preorden();
    }
 }

 class NodoABB<E extends Comparable<E>> {
     final E value;
     NodoABB<E> left,
                rigth;

    public NodoABB(E value) {
        super();
        this.value = value;
    }
    public NodoABB(E value, NodoABB<E> left, NodoABB<E> rigth) {
        this.value = value;
        this.left = left;
        this.rigth = rigth;
    }
 }