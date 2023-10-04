from Ejercicios_Python.ejercicio6 import calcular_iva_y_importe

def test_calculo_iva_y_importe():
    iva, importe_sin_iva = calcular_iva_y_importe(100)
    assert iva == 10
    assert importe_sin_iva == 90