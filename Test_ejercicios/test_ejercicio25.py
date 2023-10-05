from Ejercicios_Python.ejercicio25 import fecha_nacimiento

def test_fecha_nacimiento():
    assert fecha_nacimiento("01", "10", "2001") == "Día: 01, Mes: 10, Año: 2001"