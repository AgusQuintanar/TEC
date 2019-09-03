public class MiListaEnlazada<E> {
    private NodoLE<E> first,
                      last;
    private int size;

    public MiListaEnlazada() {
        this.first = this.last = null;
        this.size = 0;
    }

    //Tarea
    public MiListaEnlazada(E[] valores) {

    }

    public E first() {
        return this.first.dato;
    }

    public E last() {
        return this.last.dato;
    }
    public boolean isEmpty() {
        return this.size == 0;
    }

    public void insertAtFirst(E dato) {
        this.first = new NodoLE<>(dato, this.first);
        this.size++;
        if (this.size == 1) this.last = this.first;
    }

    public void insertAtLast(E dato) {

    }

    public void insertAt(E dato, int pos) {

    }

    public E removeFirst() {
        try {
            E dato = this.first();
            this.first = this.first.next;
            this.size--;
            return dato;
        } catch (NullPointerException e) {

        }
    }
    public static void main(String[] args) {
        
    }
}

class NodoLE<E> {
    E dato;
    NodoLE<E> next;

    public NodoLE(E dato, NodoLE<E> next) {
        this.dato = dato;
        this.next = next;
    }

    public NodoLE(E dato) {
		this(dato,null);
	}
	
	
	public void setNext(NodoLE next) {
		this.next = next;
	}
	
	public void setDato(E dato) {
		this.dato = dato;
	}
	
	public E getDato() {
		return this.dato;
	}
	
	public NodoLE getNext() {
		return this.next;
	}
	
	public String toString() {
		return this.dato+" , "+this.next;
	}
}
