def calcular_iva(sin_iva, tipo_iva):
    iva = (sin_iva * tipo_iva) / 100
    total = sin_iva + iva
    return total

if __name__ == "__main__":
    sin_iva = float(input("Ingresa el importe sin IVA del artículo: "))
    tipo_iva = float(input("Ingresa el tipo de IVA a aplicar (porcentaje): "))
    total = calcular_iva(sin_iva, tipo_iva)
    print("El precio final del artículo con " + str(tipo_iva) + "% de IVA es: " + str(total) + " euros.")
