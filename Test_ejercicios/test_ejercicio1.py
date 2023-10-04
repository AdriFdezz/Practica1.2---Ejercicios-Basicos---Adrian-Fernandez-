from Ejercicios_Python.ejercicio1 import bienvenida

def test_bienvenida():
    resultado = bienvenida("Adri")
    assert resultado == "Hola, Adri."