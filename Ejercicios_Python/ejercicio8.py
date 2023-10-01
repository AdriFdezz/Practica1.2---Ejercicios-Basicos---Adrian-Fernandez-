def suma2(numero1, numero2):
    sumar = numero1 + numero2
    return sumar

if __name__ == "__main__":
    numero1 = int(input("Escribe el numero 1: "))
    numero2 = int(input("Escribe el numero 2: ")) + int(input("Escribe el numero 3: "))
    print("La suma de los 3 numeros es: " + str(suma2(numero1, numero2)))