from Ejercicios_Python.ejercicio1 import hola
from Ejercicios_Python.ejercicio2 import suma

def test_hola(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda nombre: "adri")
    assert hola() == "hola adri"

def test_suma (monkeypatch):
      monkeypatch.setattr('builtins.input', lambda numero: "11")
      assert suma() == "tu numero es 11"