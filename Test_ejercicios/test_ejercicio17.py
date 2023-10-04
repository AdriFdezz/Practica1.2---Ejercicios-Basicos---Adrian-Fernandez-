from Ejercicios_Python.ejercicio17 import imprimir_nombre

def test_imprimir_nombre():
    nombre = "Adrian"
    numero = 3
    resultado = imprimir_nombre(nombre, numero)
    salida = "Adrian\nAdrian\nAdrian\n"
    assert resultado == salida