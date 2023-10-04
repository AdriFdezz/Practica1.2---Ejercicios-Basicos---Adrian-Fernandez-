from Ejercicios_Python.ejercicio16 import calcular_descuento_barras

def test_calcular_descuento_barras():
    barras_no_frescas = 4
    costo = calcular_descuento_barras(barras_no_frescas)
    assert round(costo, 2) == 8.38