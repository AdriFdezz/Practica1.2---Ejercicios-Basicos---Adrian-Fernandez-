from Ejercicios_Python.ejercicio18 import cambiar_nombre

def test_transformar_nombre():
    resultado = cambiar_nombre("AdriAN fernANdez gaRRido")
    assert resultado == ("adrian fernandez garrido", "ADRIAN FERNANDEZ GARRIDO", "Adrian Fernandez Garrido")