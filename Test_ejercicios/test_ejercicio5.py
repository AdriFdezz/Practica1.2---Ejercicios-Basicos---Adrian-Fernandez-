from Ejercicios_Python.ejercicio5 import calcular_iva

def test_calculo_iva():
    resultado = calcular_iva(10, 21)
    assert resultado == 12.1