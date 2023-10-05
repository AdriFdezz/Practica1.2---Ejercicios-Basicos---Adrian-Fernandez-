from Ejercicios_Python.ejercicio24 import euros_y_centimos

def test_euros_y_centimos():
    assert euros_y_centimos(10.50) == (10, 50)