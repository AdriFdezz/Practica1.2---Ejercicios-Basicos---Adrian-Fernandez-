from Ejercicios_Python.ejercicio3 import operaciones

def test_operaciones():
    resultado = operaciones()
    salida = "Operacion 1: 8.5\nOperacion 2: 8\nOperacion 3: 4.0\nOperacion 4: 11"
    assert resultado == salida