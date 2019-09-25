import java.util.NoSuchElementException;

public class MyQueue<E> {

    private MiListaEnlazada<E> lista;

    public MyQueue() {
        this.lista = new MiListaEnlazada<>();
    }

    public int size() {
        return this.lista.size();
    }

    public boolean isEmpty() {
        return this.lista.isEmpty();
    }

    public void flush() {
        this.lista = new MiListaEnlazada<>();
        System.gc();
    }

    public void enqueue(E dato) {
        this.lista.insertAtLast(dato);
    }

    public E dequeue() {
        try {
            return this.lista.removeFirst();
        } catch (NoSuchElementException e) {
            throw new NoSuchElementException("No se puede hacer un dequeue de una cola vacia");
        }
        
    }

    public E next() {
        try {
            return this.lista.first();
        } catch (NoSuchElementException e) {
            throw new NoSuchElementException("No se puede hacer un next de una cola vacia");
        } 
    }

    public static void main(String[] args) {
        MyQueue<String> cola = new MyQueue<>(); 
        cola.enqueue("J");
        cola.enqueue("C");
        cola.enqueue("O");
        cola.enqueue("L");
        cola.enqueue("A");
        cola.enqueue("R");
        cola.enqueue("S");

        while (!cola.isEmpty()) {
            System.out.print(cola.dequeue()+",");
        }
        System.out.println();
        cola.dequeue();

    }
}