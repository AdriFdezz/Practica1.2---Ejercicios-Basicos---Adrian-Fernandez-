#Escribe un programa que pida el importe final de un artículo y calcule e imprima por pantalla el IVA que se ha pagado 
#y el importe sin IVA (suponiendo que se ha aplicado un tipo de IVA del 10%)

def calcular_iva_y_importe(final):
    tipo_iva = 10
    iva =(final * tipo_iva) / 100
    importe_sin = final - iva
    return iva, importe_sin

if __name__ == "__main__":
    final = float(input("Ingresa el importe final del artículo: "))
    iva, sin_iva = calcular_iva_y_importe(final)
    print("IVA pagado: " + str(iva) + " euros")
    print("Importe sin IVA: " + str(sin_iva) + " euros")