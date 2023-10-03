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
from Ejercicios_Python.ejercicio11 import calcular_suma_n
from Ejercicios_Python.ejercicio12 import imc
from Ejercicios_Python.ejercicio13 import division
from Ejercicios_Python.ejercicio14 import calcular_peso
from Ejercicios_Python.ejercicio15 import calcular_interes
from Ejercicios_Python.ejercicio16 import calcular_descuento_barras

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

def test_calcular_suma_n():
    resultado = calcular_suma_n(10)
    assert resultado == 55

def test_calculo_imc():
    resultado = imc(60, 1.6)
    assert resultado == 23.0

def test_division():
    resultado = division(13, 2)
    assert resultado == (6, 1)

def test_calcular_peso():
    resultado = calcular_peso(5, 3)
    assert resultado == 785

def test_calcular_interes():
    capital = 1000.0
    interes = 0.04
    ahorros = calcular_interes(capital, interes)
    assert round(ahorros[0], 2) == 1040.0
    assert round(ahorros[1], 2) == 1081.6
    assert round(ahorros[2], 2) == 1124.86

def test_calcular_descuento_barras():
    barras_no_frescas = 4
    costo = calcular_descuento_barras(barras_no_frescas)
    assert round(costo, 2) == 8.38