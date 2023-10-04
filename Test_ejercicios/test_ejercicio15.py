from Ejercicios_Python.ejercicio15 import calcular_interes

def test_calcular_interes():
    capital = 1000.0
    interes = 0.04
    ahorros = calcular_interes(capital, interes)
    assert round(ahorros[0], 2) == 1040.0
    assert round(ahorros[1], 2) == 1081.6
    assert round(ahorros[2], 2) == 1124.86