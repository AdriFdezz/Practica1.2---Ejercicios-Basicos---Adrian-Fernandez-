#Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla 
#en líneas distintas el nombre del usuario tantas veces como el número introducido.

def imprimir_nombre(nombre, numero):
    return (nombre + "\n") * numero 

if __name__ == "__main__":
    nombre = input("Ingrese su nombre: ")
    numero = int(input("Ingrese el número de veces que quieres repetirlo: "))
    imprimir_nombre(nombre, numero)
    print(imprimir_nombre(nombre, numero))