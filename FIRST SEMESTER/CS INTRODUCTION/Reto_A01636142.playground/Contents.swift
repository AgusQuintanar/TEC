import UIKit
import Foundation

//Ejercicio 1
func checarRepeticion (num: Int, listaNum: [Int]) -> Int{
    var contador = 0
    for x in 0..<listaNum.count {
        if listaNum[x] == num {
            contador += 1
        }
    }
    return contador
}
var respuestaEjercicio1 = "Se repite \(checarRepeticion(num: 3, listaNum: [5,3,8,4,5,4,4,4,4,5])) vece(s)"
print(respuestaEjercicio1)

//Ejercicio 2
func calcularMasaCorporal (nombre: String, estaturaMetros: Float, pesoKg: Float) -> String{
    let imc = pesoKg / pow(estaturaMetros,2)
    return "El indice de masa corporal de \(nombre) es de \(imc))"
}
var respuestaEjercicio2 = calcularMasaCorporal(nombre: "Pedro", estaturaMetros: 1.78, pesoKg: 72)
print(respuestaEjercicio2)

//Ejercicio 3
func regresarUbicaciones (lista: [String]) -> String{
    var ubicaciones = "Los elementos que inician con \"ho/Ho\" se encuentra en las posiciones: "
    for x in 0..<lista.count {
        if (lista[x].lowercased()).hasPrefix("ho") == true{
            ubicaciones += lista[x] + " en " + String(x+1) + " --- "
        }
    }
    return ubicaciones
}
var respuestaEjercicio3 = regresarUbicaciones(lista: ["hola","bongo","TIES","hongo","hoy","humo"," ", "Homero"])
print(respuestaEjercicio3)
