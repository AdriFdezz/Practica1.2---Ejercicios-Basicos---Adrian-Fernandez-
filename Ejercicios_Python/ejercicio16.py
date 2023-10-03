#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. 
#Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
#Después el programa debe mostrar el precio habitual de una barra de pan (establecido en el programa como una constante), 
#el descuento que se le hace por no ser fresca y el coste final total de todas las barras no frescas.

PRECIO_PAN = 3.49
DESCUENTO = 0.60

def calcular_descuento_barras(barras_no_frescas):
    coste_total = barras_no_frescas * PRECIO_PAN * DESCUENTO
    return coste_total

if __name__ == "__main__":
    barras_no_frescas = int(input("Ingrese el número de barras no frescas vendidas: "))
    coste = calcular_descuento_barras(barras_no_frescas)

    print("Precio habitual de una barra de pan: " + str(PRECIO_PAN) + " euros")
    print("Descuento por no ser del dia: " + str(DESCUENTO * 100) + "%")
    print("Coste total de las barras no frescas: " + str(round(coste, 2)) + " euros")
