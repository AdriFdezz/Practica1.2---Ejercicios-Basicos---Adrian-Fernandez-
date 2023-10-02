#Escribir un programa que lea un entero positivo, n, introducido por el usuario 
#y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. 
#La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:



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
