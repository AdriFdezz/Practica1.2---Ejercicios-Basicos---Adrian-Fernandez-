def bienvenida(nombre):
    return "Hola, " + nombre + "."

if __name__ == "__main__":
    nombre = input("Escribe tu nombre: ")
    mensaje = bienvenida(nombre)
    print(mensaje)
