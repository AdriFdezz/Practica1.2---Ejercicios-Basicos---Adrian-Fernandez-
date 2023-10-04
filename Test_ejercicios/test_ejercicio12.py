from Ejercicios_Python.ejercicio12 import imc

def test_imc():
    resultado = imc(60, 1.6)
    assert resultado == 23.0