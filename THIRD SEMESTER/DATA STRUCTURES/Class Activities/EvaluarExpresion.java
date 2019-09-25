/*******************************************
 * Agustin Salvador Quintanar de la Mora   *
 * A01636142                               *
 * Clase: EvaluarExpresion.java            *
 ******************************************/
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.LinkedList;
import java.util.Arrays;

public class EvaluarExpresion {
    private String expresionInfija;

    public EvaluarExpresion(String exInf) {
        this.expresionInfija = exInf;
    }

    public void setExpresionInfija(String exInf) {
        this.expresionInfija = exInf;
    }
    public double evaluaExpresion() {
        LinkedList<String> listaExpPost = new LinkedList<>(Arrays.asList(expresionPostfijo().split(" ")));
        int indice = 2; //Inicia en el indice 2 porque siempre empieza el postfijo con 2 numeros
        while (listaExpPost.size() != 1) {
            String dato = listaExpPost.get(indice);
            if(!dato.matches("[*+-/()^]")) indice++;
            else {
                if (dato.compareTo("+")==0) listaExpPost.set(indice-2, Double.toString(Double.parseDouble(listaExpPost.get(indice-2)) + Double.parseDouble(listaExpPost.remove(indice-1))));
                else if (dato.compareTo("-")==0) listaExpPost.set(indice-2, Double.toString(Double.parseDouble(listaExpPost.get(indice-2)) - Double.parseDouble(listaExpPost.remove(indice-1))));
                else if (dato.compareTo("*")==0) listaExpPost.set(indice-2, Double.toString(Double.parseDouble(listaExpPost.get(indice-2)) * Double.parseDouble(listaExpPost.remove(indice-1))));
                else if (dato.compareTo("/")==0) listaExpPost.set(indice-2, Double.toString(Double.parseDouble(listaExpPost.get(indice-2)) / Double.parseDouble(listaExpPost.remove(indice-1))));
                else if (dato.compareTo("^")==0) listaExpPost.set(indice-2, Double.toString(Math.pow(Double.parseDouble(listaExpPost.get(indice-2)),Double.parseDouble(listaExpPost.remove(indice-1)))));
                listaExpPost.remove(indice-1); // Elimina el operador
                indice--;
            }
        }
        return Double.parseDouble(listaExpPost.getFirst());
    }

    public String expresionPostfijo() {
        String[] exInfArr = this.expresionInfija.split(" ");

        Map<String,Integer> operadores = new HashMap<>(); 
        operadores.put("+", 1);
        operadores.put("-", 1);
        operadores.put("*", 2);
        operadores.put("/", 2);
        operadores.put("^", 3);
        operadores.put("(", 0);

        MyStack<String> pila = new MyStack<>();
        MiListaEnlazada<String> lista = new MiListaEnlazada<>();

        for (int i=0; i <exInfArr.length; i++) { //Recorre el array de la expresion infija
            if (!exInfArr[i].matches("[*+-/()^]")) lista.insertAtLast(exInfArr[i]); //Si el dato actual es numerico se inserta a la lista
            else if (exInfArr[i].compareTo("(")==0 || pila.isEmpty()) pila.push(exInfArr[i]);//Si el dato actual es un parentesis abierto o es un operador y la pila esta vacia, se inserta a la pila
            else if (exInfArr[i].compareTo(")")==0) { //Si el dato actual es un parentesis cerrado
                while (pila.top().compareTo("(")!=0) lista.insertAtLast(pila.pop()); //Mientras que el top de la pila no sea un parentesis abierto inserta a la lista todos los operadores y los elimina de la pila
                pila.pop(); //Elimina el parentesis abierto en el top de la pila
            } else { 
                while (!pila.isEmpty() && operadores.get(exInfArr[i]) <= operadores.get(pila.top())) lista.insertAtLast(pila.pop()); //Mete todos los operadores de menor jerarquia a la lista y los elimina de la pila
                pila.push(exInfArr[i]); //Inserta el operador en la pila
            }
        }
        while (!pila.isEmpty()) lista.insertAtLast(pila.pop()); //Inserta los operadores que quedan en la lista y los elimina de la pila

        String expPostfijo = "";
        int tmno = lista.size();
        for (int i=0; i<tmno;i++) expPostfijo += lista.removeFirst() + " "; //Convierte la lista enlazada a un string
 
        return expPostfijo;
    }
}