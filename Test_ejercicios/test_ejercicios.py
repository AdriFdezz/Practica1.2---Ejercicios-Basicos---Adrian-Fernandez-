from Ejercicios_Python.ejercicio1 import bienvenida
from Ejercicios_Python.ejercicio2 import importe_total
from Ejercicios_Python.ejercicio3 import operaciones
from Ejercicios_Python.ejercicio4 import conversor_fahrenheit
from Ejercicios_Python.ejercicio5 import calcular_iva
from Ejercicios_Python.ejercicio6 import calcular_iva_y_importe
from Ejercicios_Python.ejercicio7 import suma
from Ejercicios_Python.ejercicio8 import suma2
from Ejercicios_Python.ejercicio9 import suma3
from Ejercicios_Python.ejercicio10 import calcular_fraccion

def test_bienvenida():
    resultado = bienvenida("Adri")
    assert resultado == "Hola, Adri."

def test_importe_total():
    horas_trabajo = "5"
    dinero_horas = "5"
    resultado = importe_total(horas_trabajo, dinero_horas)
    salida= "\nhoras de trabajo: 5\nCoste por horas: 5\nImporte total: 25.0"
    assert resultado == salida

def test_operaciones():
    resultado = operaciones()
    salida = "Operacion 1: 8.5\nOperacion 2: 8\nOperacion 3: 4.0\nOperacion 4: 11"
    assert resultado == salida

def test_conversor_fahrenheit():
    resultado = conversor_fahrenheit(30)
    assert resultado == 86

def test_calculo_iva():
    resultado = calcular_iva(10, 21)
    assert resultado == 12.1

def test_calculo_iva_y_importe():
    iva, importe_sin_iva = calcular_iva_y_importe(100)
    assert iva == 10
    assert importe_sin_iva == 90

def test_suma():
    resultado = suma(1, 2, 3)
    assert resultado == 6

def test_suma2():
    resultado = suma2(2, 3)
    assert resultado == 5

def test_suma3():
    resultado = suma3(5, 5)
    assert resultado == 10

def test_calcular_fraccion():
    resultado = calcular_fraccion()
    assert resultado == 0.25