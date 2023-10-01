from Ejercicios_Python.ejercicio1 import bienvenida
from Ejercicios_Python.ejercicio2 import importe_total
from Ejercicios_Python.ejercicio3 import operaciones
from Ejercicios_Python.ejercicio4 import Conversor_fahrenheit

def test_bienvenida():
    resultado = bienvenida("Adri")
    assert resultado == "Hola, Adri."

def test_importe_total():
    horas_trabajo = "5"
    dinero_horas = "5"
    resultado = importe_total(horas_trabajo, dinero_horas)
    salida= "\nhoras de trabajo: 5\nCoste por horas: 5\nImporte total: 25.0"
    assert resultado == salida

def test_operaciones():
    resultado = operaciones()
    salida = "Operacion 1: 8.5\nOperacion 2: 8\nOperacion 3: 4.0\nOperacion 4: 11"
    assert resultado == salida

def test_conversor_fahrenheit():
    resultado = Conversor_fahrenheit(30)
    assert resultado == 86