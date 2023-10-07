from Ejercicios_Python.ejercicio26 import cesta_compra

def test_cesta_compra():
    assert cesta_compra("leche, azucar, pan, fruta") == ["leche", " azucar", " pan", " fruta"]