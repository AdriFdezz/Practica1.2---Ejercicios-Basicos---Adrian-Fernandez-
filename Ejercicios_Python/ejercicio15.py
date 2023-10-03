#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
#Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta 
#de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, 
#introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros
#tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

def calcular_interes(capital, interes):
    ahorros_anuales = []
    for _ in range(3):
        capital = capital * (1 + interes)
        ahorros_anuales.append(capital)
    return ahorros_anuales

if __name__ == "__main__":
    capital = float(input("Ingresa la cantidad de dinero depositada: "))
    interes = 0.04
    ahorros = calcular_interes(capital, interes)

    print("Ahorros después del primer año: " + str(round(ahorros[0], 2)))
    print("Ahorros después del segundo año: " + str(round(ahorros[1], 2)))
    print("Ahorros después del tercer año: " + str(round(ahorros[2], 2)))
