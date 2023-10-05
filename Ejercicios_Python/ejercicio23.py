#Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) 
#pero con dominio ceu.es.

def cambiar_correo(correo):
    partes = correo.split('@')
    
    if len(partes) == 2:
        nuevo_correo = partes[0] + "@ceu.es"
        return nuevo_correo

if __name__ == "__main__":
    correo = input("Introduce tu correo electrónico: ")
    nuevo_correo = cambiar_correo(correo)
    print("Nuevo correo electrónico:", nuevo_correo)
