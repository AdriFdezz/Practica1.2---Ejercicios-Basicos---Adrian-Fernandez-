#Escribe un programa que solicite tres números al usuario y calcule e imprima por pantalla su suma.

def suma(numero1, numero2, numero3):
    sumar = numero1 + numero2 + numero3
    return sumar

if __name__ == "__main__":
    numero1 = int(input("Escribe el numero 1: "))
    numero2 = int(input("Escribe el numero 2: "))
    numero3 = int(input("Escribe el numero 3: "))
    print("La suma de los 3 numeros es: " + str(suma(numero1, numero2, numero3)))