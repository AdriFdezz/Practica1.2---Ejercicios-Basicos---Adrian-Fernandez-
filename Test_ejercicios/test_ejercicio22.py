from Ejercicios_Python.ejercicio22 import cambiar_vocal

def test_cambiar_vocal():
    assert cambiar_vocal("Hola, esto es una prueba", "e") == "Hola, Esto Es una pruEba"