from Ejercicios_Python.ejercicio20 import obtener_numero

def test_obtener_numero():
    telefono = "+34-123456789-12"
    resultado = obtener_numero(telefono)
    assert resultado == "123456789"