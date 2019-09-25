/*******************************************
 * Agustin Salvador Quintanar de la Mora   *
 * A01636142                               *
 * Clase: MiListaEnlazada.java             *
 ******************************************/

import java.util.NoSuchElementException;

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
        for (int i=0; i<valores.length; i++) {
            insertAtLast(valores[i]);
        }
    }

    public E first() throws NoSuchElementException{
        try {
            return this.first.dato;
        } catch (NullPointerException e) {
            throw new NoSuchElementException("No se puede borrar el primer elemento de una lista vacia");
        }
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
        if(this.size == 0) this.insertAtFirst(dato);
        else {
            NodoLE<E> nvo = new NodoLE<>(dato);
            this.last.setNext(nvo);
            this.last = nvo;
            this.size++;  
        }
    }

    public void insertAt(E dato, int pos) {
        if(pos < 0 || pos >= size) {
			throw new IndexOutOfBoundsException("Indice no valido");
        }
        else if(pos == 0 || this.size == 0) {
            this.insertAtFirst(dato);
        } 
        else {
            try {
                NodoLE<E> nodoActual = this.first;
                    
                for(int i=0; i < pos - 1; i++) {
                    nodoActual = nodoActual.getNext();
                }
                NodoLE<E> nodoTemp = nodoActual.next;
                nodoActual.setNext(new NodoLE<E>(dato));
                nodoActual.next.setNext(nodoTemp);
                this.size++;
            
    
            } catch(NullPointerException e) { 
            System.out.print("");
            }
        }
	    
    }

    public E removeFirst() {
        try {
            E dato = this.first();
            this.first = this.first.next;
            this.size--;
            if (this.size == 0) this.last = null;
            return dato;
        } catch (NullPointerException e) {
            throw new NoSuchElementException("No se puede borrar el primer elemento de una lista vacia");
        } 
    }

    public String toString() { 
        NodoLE currNode = this.first; 
        String res = "";
        while (currNode != null) { 
           res += currNode.dato + " "; 
            currNode = currNode.next; 
        } 
        return res;
    } 

    public E removeLast() throws NoSuchElementException{
        try {
            E dato = this.last();
            NodoLE<E> nodoActual = this.first;
            for (int i=0; i<this.size-2; i++) nodoActual = nodoActual.getNext();
            nodoActual.setNext(null);
            this.last = nodoActual;
            this.size--;
            return dato;
        } catch (NullPointerException e) {
            throw new NoSuchElementException("No se puede borrar el primer elemento de una lista vacia");
        } 

    }

    public E removeAt(int pos) throws NoSuchElementException{
        if (this.size <= 1) {
            return this.removeFirst();
        }
        else if (pos == this.size - 1) {
            return this.removeLast();
        }
        else {
            NodoLE<E> current = this.first;
            E dato;
            for (int i=0; i<pos-1; i++) {
                current = current.getNext();
            }
            dato = current.getNext().getDato();
            current.setNext(current.getNext().getNext());
            this.size--;
            return dato;
        }
    }

    public int size() {
        return this.size;
    }

    public void setAt(E dato, int pos) {
        
    }

    public static void main(String[] args) {
        Integer[] a = {1,2,3,4,5};
        MiListaEnlazada le = new MiListaEnlazada<>(a);
        System.out.println("Size: "+le.size);
        System.out.println(le);
        le.insertAt("hola", 1);
        System.out.println(le);


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
	
	public NodoLE <E> getNext() {
		return this.next;
	}
	
	public String toString() {
		return this.dato+" , "+this.next;
	}
}
