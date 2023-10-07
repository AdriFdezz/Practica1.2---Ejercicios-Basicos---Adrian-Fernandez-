from Ejercicios_Python.ejercicio27 import calcular_productos

def test_calcular_productos():
    resultado = calcular_productos("Jamon", 7.50, 5)
    assert resultado == "Nombre del producto: Jamon\nPrecio unitario: 7.50\nNúmero de unidades: 005\nCoste total: 37.50"