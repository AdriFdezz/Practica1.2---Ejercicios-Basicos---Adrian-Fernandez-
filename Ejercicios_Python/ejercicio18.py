#Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla 
#el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas 
#y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre 
#combinando mayúsculas y minúsculas como quiera.

def cambiar_nombre(nombre):
    nombre_minusculas = nombre.lower()
    nombre_mayusculas = nombre.upper()
    palabras = nombre.split()
    palabras_primera_mayus = [palabra.capitalize() for palabra in palabras]
    nombre_primera_mayus = " ".join(palabras_primera_mayus)
    return nombre_minusculas, nombre_mayusculas, nombre_primera_mayus

if __name__ == "__main__":
    nombre_completo = input("Escribe el nombre completo: ")
    nombre_minusculas, nombre_mayusculas, nombre_primera_mayus = cambiar_nombre(nombre_completo)
    print("Nombre en minúsculas:", nombre_minusculas)
    print("Nombre en mayúsculas:", nombre_mayusculas)
    print("Nombre con la primera letra en mayusculas:", nombre_primera_mayus)
