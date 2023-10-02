def calcular_suma_n(n):
    suma = (n * (n + 1)) // 2
    return suma

if __name__ == "__main__":
    n = int(input("Ingresa un entero positivo n: "))

    if n <= 0:
        print("Ingresa un entero positivo.")
    else:
        resultado = calcular_suma_n(n)
        print("La suma de los enteros desde 1 hasta " + str(n) + " es: " + str(resultado))
