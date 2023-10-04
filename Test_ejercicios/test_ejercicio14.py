from Ejercicios_Python.ejercicio14 import calcular_peso

def test_calcular_peso():
    resultado = calcular_peso(5, 3)
    assert resultado == 785