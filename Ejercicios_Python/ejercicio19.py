#Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario 
#lo introduzca muestre por pantalla "NOMBRE tiene n letras.", donde NOMBRE es el nombre de usuario en mayúsculas y n 
#es el número de letras que tienen el nombre.

def contar_letras(nombre):
    return len(nombre)

if __name__ == "__main__":
    nombre = input("Introduce tu nombre para contar sus letras: ")
    nombre_mayusculas = nombre.upper()
    cantidad_letras = contar_letras(nombre)
    mensaje = nombre_mayusculas + " tiene " + str(cantidad_letras) + " letras."
    print(mensaje)
