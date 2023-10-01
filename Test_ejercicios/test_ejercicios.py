from Ejercicios_Python.ejercicio1 import bienvenida
from Ejercicios_Python.ejercicio2 import importe_total

def test_bienvenida():
    resultado = bienvenida("Adri")
    assert resultado == "Hola, Adri."

def test_importe_total():
    horas_trabajo = "5"
    dinero_horas = "5"
    resultado = importe_total(horas_trabajo, dinero_horas)
    salida= "\nhoras de trabajo: 5\nCoste por horas: 5\nImporte total: 25.0"
    assert resultado == salida